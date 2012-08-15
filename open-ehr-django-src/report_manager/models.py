from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from open-ehr.registration.models import *
from open-ehr.accounts.models import UserProfile
class ReportResultsManager(models.Manager):
    def create_inactive_patient(self,user_mobile,user_dob,created_by):

        try:
            new_patient_type_user = User.objects.get(username__iexact=user_mobile)
        except User.DoesNotExist:
            new_patient_type_user = User.objects.create_user(user_mobile,"","password")
            new_patient_type_user.is_active = False
            new_patient_type_user.save()
            new_patient_type_user_profile = UserProfile(user=new_patient_type_user,dob=user_dob,created_by=created_by,belongs_to_lab=created_by.get_profile().belongs_to_lab,is_lab_super_user=True,is_doctor=False,is_technician=False,is_patient=False,needs_pin_to_login=False,pin_exists=False,pin_permanent='123456')
            #new_patient_type_user_profile = UserProfile(user_id=new_patient_type_user.id,added_by_lab=open-ehrhx_super_user,is_doctor=False,is_technician=False,needs_pin_to_login=True,pin_exists=False,pin_permanent='1234')
            new_patient_type_user_profile.save()





class ReportTypes(models.Model):
    def __unicode__(self):
        return self.report_name
    report_name = models.CharField(max_length=100)
    report_element_json_list = models.TextField(max_length=1000)
    report_belongs_to_lab = models.ForeignKey(User)

    class Meta:
        unique_together = (('report_name','report_belongs_to_lab'))
    def natural_key(self):
        return (self.report_name,)+self.report_belongs_to_lab.natural_key()


class ReportElementCategories(models.Model):
    report_element_category_name = models.CharField(max_length=200)
    #report_element_description = models.TextField(default='null')
    report_type_list_of_test_json = models.TextField()
    #report_types_json = models.TextField()



class ReportElementTests(models.Model):
    test_name = models.CharField(max_length=200)
    #report_elements_json = models.TextField()

class ReportResults(models.Model):
    lab_owner = models.ForeignKey(User,related_name='lab')
    user_mobile = models.CharField(max_length=11)
    user_dob = models.CharField(max_length=11)
    report_type = models.ForeignKey(ReportTypes,editable=False)
    result_field = models.TextField()
    objects = ReportResultsManager()
