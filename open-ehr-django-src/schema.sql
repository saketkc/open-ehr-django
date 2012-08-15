-- phpMyAdmin SQL Dump
-- version 3.4.5deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 05, 2012 at 10:16 PM
-- Server version: 5.1.58
-- PHP Version: 5.3.6-13ubuntu3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `new_open-ehrhx`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_labsuperusers`
--

CREATE TABLE IF NOT EXISTS `accounts_labsuperusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lab_id` varchar(10) NOT NULL,
  `lab_super_user_id` int(11) NOT NULL,
  `lab_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lab_super_user_id` (`lab_super_user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `accounts_labsuperusers`
--

INSERT INTO `accounts_labsuperusers` (`id`, `lab_id`, `lab_super_user_id`, `lab_name`) VALUES
(1, 'SalusLab2', 2, 'fedora'),
(2, 'SalusLab3', 3, 'Saket'),
(3, 'SalusLab8', 8, 'Saket'),
(4, 'SalusLab9', 9, 'Saket');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_userprofile`
--

CREATE TABLE IF NOT EXISTS `accounts_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `dob` date NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `belongs_to_lab_id` int(11) NOT NULL,
  `is_lab_super_user` tinyint(1) NOT NULL,
  `is_doctor` tinyint(1) NOT NULL,
  `is_technician` tinyint(1) NOT NULL,
  `is_patient` tinyint(1) NOT NULL,
  `needs_pin_to_login` tinyint(1) NOT NULL,
  `pin_exists` tinyint(1) NOT NULL,
  `pin_permanent` varchar(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `accounts_userprofile_4a21cf42` (`created_by_id`),
  KEY `accounts_userprofile_469b5796` (`belongs_to_lab_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `accounts_userprofile`
--

INSERT INTO `accounts_userprofile` (`id`, `user_id`, `dob`, `created_by_id`, `belongs_to_lab_id`, `is_lab_super_user`, `is_doctor`, `is_technician`, `is_patient`, `needs_pin_to_login`, `pin_exists`, `pin_permanent`) VALUES
(1, 2, '1000-01-01', 1, 2, 1, 0, 0, 0, 0, 0, 'health'),
(2, 3, '1000-01-01', 2, 2, 1, 0, 0, 0, 0, 0, 'health'),
(3, 4, '1992-01-09', 3, 2, 1, 0, 0, 0, 0, 0, 'health'),
(4, 5, '1992-01-09', 3, 2, 1, 0, 0, 0, 0, 0, 'health'),
(5, 6, '1992-01-09', 3, 2, 1, 0, 0, 0, 0, 0, 'health'),
(6, 7, '1992-01-09', 3, 2, 1, 0, 0, 0, 0, 0, 'health'),
(7, 8, '1000-01-01', 2, 2, 1, 0, 0, 0, 0, 0, 'health'),
(8, 9, '1000-01-01', 2, 2, 1, 0, 0, 0, 0, 0, 'health'),
(9, 10, '1992-01-01', 3, 2, 1, 0, 0, 0, 0, 0, 'health'),
(10, 11, '1992-01-01', 3, 2, 1, 0, 0, 0, 0, 0, 'health'),
(11, 12, '2012-01-12', 3, 2, 1, 0, 0, 0, 0, 0, 'health');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'open-ehr_super_users'),
(2, 'lab_super_users'),
(3, 'lab_doctors'),
(4, 'lab_technicians'),
(5, 'lab_receptionists'),
(6, 'lab_patients_unregistered'),
(7, 'lab_patients_registered'),
(8, 'outside_doctors');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=76 ;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(33, 2, 34),
(34, 2, 35),
(35, 2, 36),
(36, 2, 37),
(37, 2, 38),
(38, 2, 7),
(39, 2, 8),
(40, 2, 9),
(41, 2, 42),
(42, 2, 39),
(43, 2, 44),
(44, 2, 45),
(45, 2, 40),
(46, 2, 43),
(47, 2, 41),
(48, 2, 28),
(49, 2, 29),
(50, 2, 30),
(52, 3, 37),
(53, 3, 38),
(54, 3, 39),
(55, 3, 40),
(56, 3, 41),
(57, 3, 42),
(58, 3, 43),
(59, 3, 44),
(60, 3, 45),
(61, 4, 37),
(62, 4, 38),
(63, 4, 39),
(64, 4, 40),
(65, 4, 41),
(66, 4, 42),
(67, 4, 43),
(68, 4, 44),
(69, 4, 45),
(70, 5, 37),
(71, 5, 38),
(72, 5, 39),
(73, 5, 40),
(74, 5, 41),
(75, 5, 42);

-- --------------------------------------------------------

--
-- Table structure for table `auth_message`
--

CREATE TABLE IF NOT EXISTS `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=52 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add message', 4, 'add_message'),
(11, 'Can change message', 4, 'change_message'),
(12, 'Can delete message', 4, 'delete_message'),
(13, 'Can add log entry', 5, 'add_logentry'),
(14, 'Can change log entry', 5, 'change_logentry'),
(15, 'Can delete log entry', 5, 'delete_logentry'),
(16, 'Can add content type', 6, 'add_contenttype'),
(17, 'Can change content type', 6, 'change_contenttype'),
(18, 'Can delete content type', 6, 'delete_contenttype'),
(19, 'Can add session', 7, 'add_session'),
(20, 'Can change session', 7, 'change_session'),
(21, 'Can delete session', 7, 'delete_session'),
(22, 'Can add site', 8, 'add_site'),
(23, 'Can change site', 8, 'change_site'),
(24, 'Can delete site', 8, 'delete_site'),
(25, 'Can add user email', 9, 'add_useremail'),
(26, 'Can change user email', 9, 'change_useremail'),
(27, 'Can delete user email', 9, 'delete_useremail'),
(28, 'Can add registration profile', 10, 'add_registrationprofile'),
(29, 'Can change registration profile', 10, 'change_registrationprofile'),
(30, 'Can delete registration profile', 10, 'delete_registrationprofile'),
(31, 'Can add report types', 11, 'add_reporttypes'),
(32, 'Can change report types', 11, 'change_reporttypes'),
(33, 'Can delete report types', 11, 'delete_reporttypes'),
(34, 'Can add report element categories', 12, 'add_reportelementcategories'),
(35, 'Can change report element categories', 12, 'change_reportelementcategories'),
(36, 'Can delete report element categories', 12, 'delete_reportelementcategories'),
(37, 'Can add report element tests', 13, 'add_reportelementtests'),
(38, 'Can change report element tests', 13, 'change_reportelementtests'),
(39, 'Can delete report element tests', 13, 'delete_reportelementtests'),
(40, 'Can add report results', 14, 'add_reportresults'),
(41, 'Can change report results', 14, 'change_reportresults'),
(42, 'Can delete report results', 14, 'delete_reportresults'),
(43, 'Can add user profile', 15, 'add_userprofile'),
(44, 'Can change user profile', 15, 'change_userprofile'),
(45, 'Can delete user profile', 15, 'delete_userprofile'),
(46, 'Can add lab super users', 16, 'add_labsuperusers'),
(47, 'Can change lab super users', 16, 'change_labsuperusers'),
(48, 'Can delete lab super users', 16, 'delete_labsuperusers'),
(49, 'Can add patient info', 17, 'add_patientinfo'),
(50, 'Can change patient info', 17, 'change_patientinfo'),
(51, 'Can delete patient info', 17, 'delete_patientinfo');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'saket', '', '', 'saket@open-ehr.com', 'sha1$05604$09c9c5633cf040cd553685e90d7fcfb71af5849b', 1, 1, 1, '2011-12-21 05:42:48', '2011-12-21 05:42:48'),
(2, 'saketkc', 'fedora', 'Hospital', 'saket.kumar@iitb.ac.in', 'sha1$91f3a$fe05afcbc123c0a859f1a6e7e16db55a1b2d8229', 0, 1, 0, '2012-01-05 03:26:12', '2011-12-21 05:43:06'),
(3, 'saket_doctor', 'Saket', 'Doctor', 'saketkc@gmail.com', 'sha1$fb119$6aeaca67fe642e49c55aa19c640619a06d6aa231', 0, 1, 0, '2011-12-22 11:22:31', '2011-12-21 05:46:48'),
(4, '9993434894', 'Mera ', 'Patient', 'saket@sakc.com', 'sha1$56747$ba53f30f9a6bc165169e776153a7cb133269e058', 0, 0, 0, '2011-12-21 05:59:14', '2011-12-21 05:59:14'),
(5, '999343489', 'SASADAA', 'dsadada', 'sad@sad,com', 'sha1$e137c$7ca7d799bbec569fe0ab80426997369e9a3e6ade', 0, 0, 0, '2011-12-21 06:22:37', '2011-12-21 06:22:37'),
(6, '9929', 'sa', 'sa', 'saket@sakc.com', 'sha1$5b511$4580ddd61bbb1f4441c4a65f2a49fc63c7a36a1c', 0, 0, 0, '2011-12-21 06:24:35', '2011-12-21 06:24:35'),
(7, '[u''9929'']', 'sa', 'sa', 'saket@sakc.com', 'sha1$e1e7f$478633090cfa9c281f340933c5b3e62dea3562ef', 0, 0, 0, '2011-12-21 06:26:07', '2011-12-21 06:26:07'),
(10, '[u''99999'']', 'sdaasd', 'dsada', 'sak@sad.com', 'sha1$f4bad$9f385856ae655ed86a58d1183cde7ef2c03ec60d', 0, 0, 0, '2011-12-21 14:55:29', '2011-12-21 14:55:29'),
(9, 'saket_technician', 'Saket', 'Techician', 'saketchoudhary@open-ehrhx.com', 'sha1$09144$addde1721464d9d1e811e131ddd3df4ef48aeca4', 0, 1, 0, '2011-12-27 19:33:56', '2011-12-21 06:48:30'),
(11, '[u''9498958943'']', 'dsadjskaldjaskdj', 'fsdjkfkjfdskjq', 'sak@sadsadada.com', 'sha1$bac5c$b2c9d40aa0a29f5d489be4c45e1910245ed19c0e', 0, 0, 0, '2011-12-21 14:56:56', '2011-12-21 14:56:56'),
(12, '[u''989876'']', 'Frwe', 'dgfd', 'qgvdw', 'sha1$9de5f$4fdef7aa4cac264de7cf86486f4c4cf58623d7d8', 0, 0, 0, '2011-12-22 11:24:27', '2011-12-22 11:24:27');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 2),
(2, 3, 3),
(3, 7, 3),
(4, 8, 3),
(5, 4, 6),
(6, 5, 6),
(7, 6, 6),
(8, 7, 6),
(9, 8, 4),
(10, 9, 4),
(11, 10, 6),
(12, 11, 6),
(13, 12, 6);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `contactus_useremail`
--

CREATE TABLE IF NOT EXISTS `contactus_useremail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(75) NOT NULL,
  `email_verfied_status` varchar(1) NOT NULL,
  `email_verification_token` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'message', 'auth', 'message'),
(5, 'log entry', 'admin', 'logentry'),
(6, 'content type', 'contenttypes', 'contenttype'),
(7, 'session', 'sessions', 'session'),
(8, 'site', 'sites', 'site'),
(9, 'user email', 'contactus', 'useremail'),
(10, 'registration profile', 'registration', 'registrationprofile'),
(11, 'report types', 'report_manager', 'reporttypes'),
(12, 'report element categories', 'report_manager', 'reportelementcategories'),
(13, 'report element tests', 'report_manager', 'reportelementtests'),
(14, 'report results', 'report_manager', 'reportresults'),
(15, 'user profile', 'accounts', 'userprofile'),
(16, 'lab super users', 'accounts', 'labsuperusers'),
(17, 'patient info', 'labs', 'patientinfo');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('fc06f26af303feb13a9e281dbc7e3883', 'YmIzZTU3ODdmOTRiOTYyNTIxYjA3NWY0ZDMyN2MzMzA0NmVmOGE5MTqAAn1xAShVDGxhYl91c2Vy\nbmFtZVgMAAAAc2FrZXRfZG9jdG9ycQJVDV9hdXRoX3VzZXJfaWSKAQNVEl9hdXRoX3VzZXJfYmFj\na2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxA3Uu\n', '2012-01-03 13:50:39'),
('b83781e48a2fd0bbdd42d2db2c89d155', 'NTBiZDg2MmY2NGRlMWM3YmZmYjU3ODY2OGY4ZWM1ZmVkMzgyZmJmNjqAAn1xAShVDGxhYl91c2Vy\nbmFtZXECWAoAAABzYWtldF90ZXN0cQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29u\ndHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQaKAQN1Lg==\n', '2012-01-02 20:44:17'),
('5a8b7b78c0324dad04247bb1a73185fe', 'NzA0ODg0OWQ2NTA5ODUzOTY1NzY0MWMzNWQzNjU1MWEzZWM0NWFiNjqAAn1xAShVDGxhYl91c2Vy\nbmFtZXECWBAAAABzYWtldF90ZWNobmljaWFucQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFu\nZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQaK\nAQl1Lg==\n', '2012-01-04 06:52:14'),
('677a69bda5c16beba0b04dded13ece5e', 'M2MxY2ZhY2FiYjg4MmRiZTJmMzY0ZWVkOGFlZDlkN2FjNDZiMjkzNTqAAn1xAShVDGxhYl91c2Vy\nbmFtZVgQAAAAc2FrZXRfdGVjaG5pY2lhbnECVRJfYXV0aF91c2VyX2JhY2tlbmRVKWRqYW5nby5j\nb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kcQNVDV9hdXRoX3VzZXJfaWSKAQl1Lg==\n', '2012-01-04 16:20:44'),
('a30dee773ff630a053d6ed20980d494c', 'M2MxY2ZhY2FiYjg4MmRiZTJmMzY0ZWVkOGFlZDlkN2FjNDZiMjkzNTqAAn1xAShVDGxhYl91c2Vy\nbmFtZVgQAAAAc2FrZXRfdGVjaG5pY2lhbnECVRJfYXV0aF91c2VyX2JhY2tlbmRVKWRqYW5nby5j\nb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kcQNVDV9hdXRoX3VzZXJfaWSKAQl1Lg==\n', '2012-01-05 06:05:24'),
('5bcdad4d0e9d8408fedeb5223da86abd', 'NzA0ODg0OWQ2NTA5ODUzOTY1NzY0MWMzNWQzNjU1MWEzZWM0NWFiNjqAAn1xAShVDGxhYl91c2Vy\nbmFtZXECWBAAAABzYWtldF90ZWNobmljaWFucQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFu\nZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQaK\nAQl1Lg==\n', '2012-01-10 19:33:57'),
('ab72bff10490ac2fd431fcf6042fee2d', 'MjllMmExMTZkNzc1NjdhOTBjMDk2ZWE0NWFjYzc1YWU4NWIwN2Q3NzqAAn1xAShVDGxhYl91c2Vy\nbmFtZXECWAcAAABzYWtldGtjcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQaKAQJ1Lg==\n', '2012-01-19 03:26:13');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `labs_patientinfo`
--

CREATE TABLE IF NOT EXISTS `labs_patientinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_first_name` varchar(20) NOT NULL,
  `patient_last_name` varchar(20) NOT NULL,
  `patient_mobile` varchar(10) NOT NULL,
  `patient_dob` date NOT NULL,
  `patient_email` varchar(40) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `report_due_on` date NOT NULL,
  `tests_json_list` longtext NOT NULL,
  `total_test_count` int(11) NOT NULL,
  `reference_doctor_name` varchar(20) NOT NULL,
  `sample_id` varchar(10) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `belongs_to_lab_id` int(11) NOT NULL,
  `technician_assigned_id` int(11) DEFAULT NULL,
  `is_complete_by_technician` tinyint(1) NOT NULL,
  `is_complete_by_doctor` tinyint(1) NOT NULL,
  `status_by_technician_json_list` longtext NOT NULL,
  `status_by_doctor_json_list` longtext NOT NULL,
  `verified_by_doctor_id` int(11) DEFAULT NULL,
  `share_count` int(11) NOT NULL,
  `shared_with_json_list` longtext NOT NULL,
  `results_field` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `labs_patientinfo_4a21cf42` (`created_by_id`),
  KEY `labs_patientinfo_469b5796` (`belongs_to_lab_id`),
  KEY `labs_patientinfo_470e25fe` (`technician_assigned_id`),
  KEY `labs_patientinfo_be98f54` (`verified_by_doctor_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `registration_registrationprofile`
--

CREATE TABLE IF NOT EXISTS `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `activation_key` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `registration_registrationprofile`
--

INSERT INTO `registration_registrationprofile` (`id`, `user_id`, `activation_key`) VALUES
(1, 2, 'ALREADY_ACTIVATED'),
(2, 3, 'ALREADY_ACTIVATED'),
(3, 4, 'bec1094c977c89c4c22a5ba2c60b3522b1627920'),
(4, 5, '08d903e3480c66ebf15cc1f8ba93e0eb7e911e3e'),
(5, 6, 'e02b8bf7602337beaa53e778412142cac0cb1f6b'),
(6, 7, '7e054f784ee9b2ca62627574ca732136d9a2a956'),
(7, 8, 'ALREADY_ACTIVATED'),
(8, 9, 'ALREADY_ACTIVATED'),
(9, 10, '8c07e95706ee11b30edc43f2bdf96e1baccc248f'),
(10, 11, '8e8ec4b67ed5c92a0a06e2674878371d9e48f8c0'),
(11, 12, '49624998bc83714088bf7ccb88ae99544f2e9b7c');

-- --------------------------------------------------------

--
-- Table structure for table `report_manager_reportelementcategories`
--

CREATE TABLE IF NOT EXISTS `report_manager_reportelementcategories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_element_category_name` varchar(200) NOT NULL,
  `report_type_list_of_test_json` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=106 ;

--
-- Dumping data for table `report_manager_reportelementcategories`
--

INSERT INTO `report_manager_reportelementcategories` (`id`, `report_element_category_name`, `report_type_list_of_test_json`) VALUES
(1, 'Absolute Eosinophil Count', '[5]'),
(2, 'Alpha 1 antitrypsin', '[7]'),
(3, 'Ammonia', '[20]'),
(4, 'Androstenedione', '[10]'),
(5, 'Androstenedione stimulation by ACTH', '[10]'),
(6, 'Arterial Blood Gas Analysis / ABG / ABGA', '[14,101,164,165,167,199]'),
(7, 'Bence Jones proteins', '[15]'),
(8, 'Bence Jones proteins Quantitative', '[121,125]'),
(9, 'Beta 2 microglobulin', '[16]'),
(10, 'Beta Hydroxy Butyrate', '[17]'),
(11, 'Blood Grouping', '[2,185]'),
(12, 'C Reactive Protein / CRP', '[52]'),
(13, 'C1 esterase inhibitor / C1 inhibitor Qualitative', '[24]'),
(14, 'C1 esterase inhibitor / C1 inhibitor Quantitative', '[24]'),
(15, 'CA 125', '[34]'),
(16, 'CA 15-3', '[35]'),
(17, 'Calcitonin', '[36]'),
(18, 'Carboxyhemoglobin', '[37]'),
(19, 'Carcinoembryonic Antigen', '[39]'),
(20, 'Ceruloplasmin', '[40]'),
(21, 'Chloride', '[42]'),
(22, 'Cholinesterase', '[46]'),
(23, 'Coagulation Profle1', '[3,4,19,38,47,112,174]'),
(24, 'Complement', '[25,26,27,28,29,30,31,32,33,80]'),
(25, 'Complement, Total CH50', '[41]'),
(26, 'Complete Blood Count', '[64,65,66,67,68,69,105,106,142,143,144,166,181,183,210]'),
(27, 'Cortisol, 12noon to 8pm', '[48]'),
(28, 'Cortisol, 8pm to 8 am', '[48]'),
(29, 'Cortisol, Free, 24 hour Urine', '[84]'),
(30, 'Cortsol, 8am to 12 noon', '[48]'),
(31, 'Creatinine Kinase', '[49,50,51]'),
(32, 'CSF analysis', '[11,54,55,59,60,61,160,165,182,201,212,214,215,216,217]'),
(33, 'Dehydroepiandrosterone / DHEA', '[57]'),
(34, 'Dehydroepiandrosterone Sulphate / DHEA Sulphate', '[58]'),
(35, 'Dihydrotestosterone', '[62]'),
(36, 'Dopamine', '[70]'),
(37, 'Epinephrine', '[72,73,74,75]'),
(38, 'Erythrocyte sedimentation rate (ESR)', '[78]'),
(39, 'Erythropoietin', '[77,145,146,147,168]'),
(40, 'Estradiol Male', '[79]'),
(41, 'Fatty Acids, free', '[81]'),
(42, 'Ferritin', '[82]'),
(43, 'Fluid Amylase', '[9]'),
(44, 'Follicle Stimulating Hormone female', '[145,146,148,168]'),
(45, 'Follicle Stimulating Hormone male', '[83]'),
(46, 'Gastrin', '[87]'),
(47, 'Glucagon', '[88]'),
(48, 'Glucose', '[90,91,92]'),
(49, 'Growth Hormone (resting)', '[94]'),
(50, 'Hemoglobin A1c', '[107]'),
(51, 'Human Chorionic Gonadotropin', '[95,96,97,98,99,100,155,186,204]'),
(52, 'Hydroxyproline Urine, 24 hours', '[109]'),
(53, 'Insulin', '[111]'),
(54, 'Ionised calcium', '[117]'),
(55, 'Iron', '[118]'),
(56, 'Iron Binding Capacity', '[119]'),
(57, 'Iron Binding Capacity Saturation', '[120]'),
(58, 'Ketone', '[122]'),
(59, 'Kidney Function Tests / Renal Function Tests', '[21,22,190]'),
(60, 'Lactate', '[123]'),
(61, 'Lactate Dehydrogenase', '[124]'),
(62, 'Lactate Dehydrogenase Isoenzymes', '[126,127,128,129,130]'),
(63, 'Leutinizing Hormone, female', '[138,139,140,168]'),
(64, 'Leutinizing Hormone, male', '[137]'),
(65, 'Lipid Profile HDL Cholesterol', '[102,103]'),
(66, 'Lipid Profile HDL/LDL Ratio', '[104]'),
(67, 'Lipid Profile LDL Cholesterol', '[131,132,133,134,135,136]'),
(68, 'Lipid Profile Total Cholesterol', '[43,44,45]'),
(69, 'Lipoprotein A', '[141]'),
(70, 'Liver Function Tests', '[1,6,8,12,63,86,110,187,191,211,213]'),
(71, 'Methemoglobin', '[149]'),
(72, 'Microalbumin, 24 hr Urine', '[150]'),
(73, 'Microalbumin, Spot Urine', '[150]'),
(74, 'Myoglobin', '[154]'),
(75, 'Norepinephrine', '[157,158,159]'),
(76, 'Norepinephrine, Urine', '[156]'),
(77, 'Oxygen Percent Saturation, Arterial', '[199]'),
(78, 'Oxygen Percent Saturation, Venous, Arm', '[162]'),
(79, 'Parathyroid Hormone', '[163]'),
(80, 'Progesterone, Female', '[170,171]'),
(81, 'Progesterone, male', '[169]'),
(82, 'Prolactin', '[172]'),
(83, 'Prostate Specific Antigen', '[175,176]'),
(84, 'Prostate Specific Antigen, free', '[177]'),
(85, 'Pyruvate', '[178]'),
(86, 'RA Factor / RAF', '[179]'),
(87, 'Reticulocyte Count', '[184]'),
(88, 'Serum Alpha fetoprotein', '[188]'),
(89, 'Serum Amylase ( Pancreatic )', '[9]'),
(90, 'Serum Electrolytes', '[189,192,193,194,195]'),
(91, 'Sex Hormone Binding Globulin', '[196]'),
(92, 'Somatostatin', '[197]'),
(93, 'Testosterone, free', '[202]'),
(94, 'Testosterone, total', '[203]'),
(95, 'Thyroid Function Tests', '[85,205,20,207,208,209,219,220]'),
(96, 'Total Hemolytic Component', '[41]'),
(97, 'Total Protein', '[173]'),
(98, 'Transferrin', '[218]'),
(99, 'Troponin I', '[56,221]'),
(100, 'Troponin T', '[56,222]'),
(101, 'Uric Acid', '[224]'),
(102, 'Urine Analysis', '[13,18,23,53,71,76,89,93,108,113,114,115,116,151,152,153,161,165,173,180,182,198,200,223,228,229,230]'),
(103, 'Urobilinogen', '[225]'),
(104, 'Vasoactive Intestinal Peptide', '[226]'),
(105, 'Vinillylmandelic Acid, Urine', '[227]');

-- --------------------------------------------------------

--
-- Table structure for table `report_manager_reportelementtests`
--

CREATE TABLE IF NOT EXISTS `report_manager_reportelementtests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=232 ;

--
-- Dumping data for table `report_manager_reportelementtests`
--

INSERT INTO `report_manager_reportelementtests` (`id`, `test_name`) VALUES
(1, '5-Hydroindoleacetic acid'),
(2, 'A:G Ratio'),
(3, 'ABO grouping'),
(4, 'Activated Clotting Time ( ACT )'),
(5, 'Activated Partial Thromboplastin Time'),
(6, 'AEC'),
(7, 'Alkaline Phosphatase'),
(8, 'Alpha 1 antitrypsin'),
(9, 'ALT, SGPT'),
(10, 'Amylase ( Pancreatic )'),
(11, 'Androstenedione'),
(12, 'Appearance'),
(13, 'AST, SGOT'),
(14, 'Bacteria'),
(15, 'Base Excess'),
(16, 'Bence Jones Protein'),
(17, 'Beta 2 microglobulin'),
(18, 'Beta Hydroxy Butyrate'),
(19, 'Bladder cells'),
(20, 'Bleeding Time (Duke''s method )'),
(21, 'Blood Ammonia'),
(22, 'Blood Urea'),
(23, 'Blood Urea Nitrogen'),
(24, 'Broad casts'),
(25, 'C1 inhibitor '),
(26, 'C1q'),
(27, 'C2'),
(28, 'C3'),
(29, 'C4'),
(30, 'C5'),
(31, 'C6'),
(32, 'C7'),
(33, 'C8'),
(34, 'C9'),
(35, 'CA 125'),
(36, 'CA 15-3'),
(37, 'Calcitonin'),
(38, 'Carboxyhemoglobin'),
(39, 'CBC'),
(40, 'CEA Carcinoembryonic antigen'),
(41, 'Ceruloplasmin'),
(42, 'CH 50'),
(43, 'Chloride'),
(44, 'Cholesterol, Borderline high'),
(45, 'Cholesterol, Desirable'),
(46, 'Cholesterol, High'),
(47, 'Cholineterase'),
(48, 'Clotting Time ( Lee and White Method )'),
(49, 'Cortisol'),
(50, 'CPK - MB fraction of total activity'),
(51, 'CPK - MB mass'),
(52, 'CPK - Total'),
(53, 'CRP'),
(54, 'Crystals'),
(55, 'CSF Pressure'),
(56, 'CSF Volume'),
(57, 'cut off for MI'),
(58, 'DHEA'),
(59, 'DHEA Sulphate'),
(60, 'Differential Leucocyte Count, Lymphocytes'),
(61, 'Differential Leucocyte Count, Monocytes'),
(62, 'Differential Leucocyte Count, Neutrophils'),
(63, 'Dihydrotestosterone'),
(64, 'Direct Bilirubin'),
(65, 'DLC Bands'),
(66, 'DLC Basophils'),
(67, 'DLC Eosinophils'),
(68, 'DLC Lymphocytes'),
(69, 'DLC Monocytes'),
(70, 'DLC Neutrophils'),
(71, 'Dopamine'),
(72, 'Eosinophils'),
(73, 'Epinephrine'),
(74, 'Epinephrine Sitting'),
(75, 'Epinephrine Standing (30 min)'),
(76, 'Epinephrine Supine (30 min)'),
(77, 'Epithelial cell casts'),
(78, 'Erythropoietin'),
(79, 'ESR'),
(80, 'Estradiol Male'),
(81, 'Factor B '),
(82, 'Fatty Acids, free'),
(83, 'Ferritin'),
(84, 'Follicle Stimulating Hormone male'),
(85, 'Free Cortisol'),
(86, 'Free Thyroxine Index'),
(87, 'Gamma Glutamyl Transferase, GGTP, GGT'),
(88, 'Gastrin'),
(89, 'Glucagon'),
(90, 'Glucose'),
(91, 'Glucose 2h Postprandial'),
(92, 'Glucose fasting'),
(93, 'Glucose Random Blood'),
(94, 'Granular casts'),
(95, 'Growth Hormone (resting)'),
(96, 'hCG 1-2 weeks postconception'),
(97, 'hCG 10-14 weeks postconception'),
(98, 'hCG 2-3 weeks postconception'),
(99, 'hCG 3-4 weeks postconception'),
(100, 'hCG 4-5 weeks postconception'),
(101, 'hCG 5-10 weeks postconception'),
(102, 'HCO3 ( Bicarbonate )'),
(103, 'HDL, High'),
(104, 'HDL, Low'),
(105, 'HDL/LDL'),
(106, 'Hematocrit/ PCV'),
(107, 'Hemoglobin'),
(108, 'Hemoglobin A1c'),
(109, 'Hyaline casts'),
(110, 'Hydroxyproline Urine'),
(111, 'Indirect Bilirubin'),
(112, 'Insulin'),
(113, 'International Normalised Ratio ( INR )'),
(114, 'Iodine, Mild deficiency'),
(115, 'Iodine, Moderate deficiency'),
(116, 'Iodine, Normal'),
(117, 'Iodine, Severe deficiency'),
(118, 'Ionised Calcium'),
(119, 'Iron'),
(120, 'Iron Binding Capacity'),
(121, 'Iron Binding Capacity Saturation'),
(122, 'Kappa chain'),
(123, 'Ketone'),
(124, 'Lactate'),
(125, 'Lactate Dehydrogenase'),
(126, 'Lambda'),
(127, 'LDH Isoenzyme Fraction 1'),
(128, 'LDH Isoenzyme Fraction 2'),
(129, 'LDH Isoenzyme Fraction 3'),
(130, 'LDH Isoenzyme Fraction 4'),
(131, 'LDH Isoenzyme Fraction 5'),
(132, 'LDL, Above Optimal'),
(133, 'LDL, Borderline High'),
(134, 'LDL, High'),
(135, 'LDL, Optimal'),
(136, 'LDL, Very High '),
(137, 'LDL, Very high risk patients'),
(138, 'LH male'),
(139, 'LH Menstruating Follicular Phase'),
(140, 'LH Menstruating Luteal Phase'),
(141, 'LH Menstruating Ovulatory Phase'),
(142, 'Lipoprotein A'),
(143, 'MCH'),
(144, 'MCHC'),
(145, 'MCV'),
(146, 'Menstruating follicular phase'),
(147, 'Menstruating luteal phase'),
(148, 'Menstruating mid-cycle peak'),
(149, 'Menstruating ovulatory phase'),
(150, 'Methemoglobin'),
(151, 'Microalbumin'),
(152, 'Microalbumin; Clinical albuminuria'),
(153, 'Microalbumin; Microalbuminuria'),
(154, 'Microalbumin; normal'),
(155, 'Myoglobin'),
(156, 'Non pregnant female'),
(157, 'Norepinephrine'),
(158, 'Norepinephrine Sitting'),
(159, 'Norepinephrine Standing (30 min)'),
(160, 'Norepinephrine Supine (30 min)'),
(161, 'Oligoclonal Bands'),
(162, 'Oxalate'),
(163, 'Oxygen Percent Saturation, Arterial'),
(164, 'Parathyroid Hormone'),
(165, 'pCO2'),
(166, 'pH'),
(167, 'Platelet count'),
(168, 'pO2'),
(169, 'Postmenopausal'),
(170, 'Progesterone '),
(171, 'Progesterone Follicular Phase'),
(172, 'Progesterone Midluteal Phase'),
(173, 'Prolactin'),
(174, 'Proteins'),
(175, 'Prothrombin Time'),
(176, 'PSA males < 40 years'),
(177, 'PSA males > 40 years'),
(178, 'PSA, free'),
(179, 'Pyruvate'),
(180, 'RAF/ RF'),
(181, 'RBC casts'),
(182, 'RBC count'),
(183, 'Red Blood Cells'),
(184, 'Red Cell Distribution width'),
(185, 'Reticulocyte'),
(186, 'Rh Grouping'),
(187, 'Second trimester'),
(188, 'Serum Albumin'),
(189, 'Serum Alpha fetoprotein '),
(190, 'Serum Calcium'),
(191, 'Serum Creatinine'),
(192, 'Serum Globulin'),
(193, 'Serum Magnesium'),
(194, 'Serum Phosphate'),
(195, 'Serum Potassium'),
(196, 'Serum Sodium'),
(197, 'Sex Hormone binding Globulin'),
(198, 'Somatostatin'),
(199, 'Specific Gravity'),
(200, 'spO2 ( Oxygen Saturation )'),
(201, 'Squamous Cells'),
(202, 'Sugar ( Glucose )'),
(203, 'Testosterone, free'),
(204, 'Testosterone, total'),
(205, 'Third trimester'),
(206, 'Thyroglobulin'),
(207, 'Thyroid Binding Globulin'),
(208, 'Thyroid Stimulating Hormone (TSH)'),
(209, 'Thyroxine, free (fT4)'),
(210, 'Thyroxine, total (T4)'),
(211, 'TLC'),
(212, 'Total Bilirubin'),
(213, 'Total Leucocyte Count'),
(214, 'Total Proteins'),
(215, 'Total Proteins, Albumin'),
(216, 'Total Proteins, Cisternal'),
(217, 'Total Proteins, Lumbar'),
(218, 'Total Proteins, Ventricular'),
(219, 'Transferrin'),
(220, 'Triiodothyronine, free (fT3)'),
(221, 'Triiodothyronine, total (T3)'),
(222, 'Troponin I Normal Population'),
(223, 'Troponin T Normal Population'),
(224, 'Tubular cells'),
(225, 'Uric Acid'),
(226, 'Urobilinogen'),
(227, 'VIP'),
(228, 'VMA'),
(229, 'Waxy casts'),
(230, 'WBC casts'),
(231, 'White Blood Cells/ Pus cells');

-- --------------------------------------------------------

--
-- Table structure for table `report_manager_reportresults`
--

CREATE TABLE IF NOT EXISTS `report_manager_reportresults` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lab_owner_id` int(11) NOT NULL,
  `user_mobile` varchar(11) NOT NULL,
  `user_dob` varchar(11) NOT NULL,
  `report_type_id` int(11) NOT NULL,
  `result_field` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `report_manager_reportresults_676e9bf4` (`lab_owner_id`),
  KEY `report_manager_reportresults_3d4f9c7e` (`report_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `report_manager_reporttypes`
--

CREATE TABLE IF NOT EXISTS `report_manager_reporttypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_name` varchar(100) NOT NULL,
  `report_element_json_list` longtext NOT NULL,
  `report_belongs_to_lab_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `report_manager_reporttypes_6afaf388` (`report_belongs_to_lab_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `report_manager_reporttypes`
--

INSERT INTO `report_manager_reporttypes` (`id`, `report_name`, `report_element_json_list`, `report_belongs_to_lab_id`) VALUES
(20, 'MAX3', '[1]', 21),
(18, 'MAX1', '[1,2]', 21);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
