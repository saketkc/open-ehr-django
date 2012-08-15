from django.conf.urls.defaults import *
import os.path
from open-ehr import settings
from django.contrib import admin
from open-ehr.accounts.views import *
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','open-ehr.contactus.views.add_user'),
    (r'^thanks/$','open-ehr.contactus.views.thanks'),
    (r'^pinlogin/$','open-ehr.registration.views.pinlogin'),
    (r'^register/$','open-ehr.registration.views.register_lab',{ 'template_name': 'registration/register.html', }, 'register_lab'),
    (r'^logout/$','open-ehr.registration.views.logout_view'),
    (r'^accounts/login/$','open-ehr.registration.views.login'),
    (r'^activate/(?P<activation_key>.*)/$','open-ehr.registration.views.activate_lab'),
    (r'^report_manager/$','open-ehr.report_manager.views.view_all_reports'),
    (r'^add_new_report_type/$','open-ehr.report_manager.views.add_new_report_type'),
    (r'^render_testelement_categories_form/$','open-ehr.report_manager.views.render_testelement_categories_form'),
    (r'^logout','open-ehr.registration.views.logout_view'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/view/(?P<username>.*)/$','open-ehr.accounts.views.view'),
    (r'^forgotpassword/$', 'open-ehr.registration.views.forgotpassword'),
    (r'^updatepassword/$', 'open-ehr.registration.views.updatepassword'),
    (r'^accounts/edit/(?P<username>.*)/$','open-ehr.accounts.views.edit'),
    (r'^accounts/delete/(?P<username>.*)/$','open-ehr.accounts.views.delete'),
    (r'^accounts/add/(?P<username>.*)/$','open-ehr.accounts.views.add'),
    (r'^labs/$','open-ehr.registration.views.labs'),
    (r'^labs/view/$','open-ehr.labs.views.view'),
    (r'^labs/add/$','open-ehr.labs.views.add'),
    (r'^labs/reports/confirm_submitted_report/$','open-ehr.labs.views.confirm_submitted_report'),
    (r'^labs/patient/view/$','open-ehr.labs.views.patient_view'),
    url(r'^labs/patient/view/view_expanded/(?P<report_id>[\d]+)/(?P<category_id>[\d]+)/$','open-ehr.labs.views.view_expanded'),    
    (r'^labs/report_lookup/$','open-ehr.labs.views.report_lookup'),
    (r'^labs/report_edit/(?P<test_number>.*)/$','open-ehr.labs.views.report_edit'),
    (r'^labs/share/(?P<report_id>.*)/$','open-ehr.labs.views.share'),
    url(r'^labs/reports/edit/(?P<report_id>[\d]+)/(?P<test_number>[\d]+)/$','open-ehr.labs.views.edit',name='edit_report'),
    url(r'^labs/reports/view_submitted_report/(?P<report_id>[\d]+)/(?P<test_number>[\d]+)/$','open-ehr.labs.views.view_submitted_report',name='view_submitted_report'),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    (r'^blog/(?P<path>.*)$', 'open-ehr.accounts.views.redirectblog'),
    (r'^change/(?P<key>.{70})/$', 'open-ehr.registration.views.change_password'),
)
