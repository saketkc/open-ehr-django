from django.db import models
from django.contrib.auth.models import User

class PatientInfo(models.Model):
    patient_first_name = models.CharField(max_length=20)
    patient_last_name = models.CharField(max_length=20)
    patient_mobile = models.CharField(max_length=10)                #
    patient_dob = models.DateField()                                #
    patient_email = models.CharField(max_length=40)                 #
    gender = models.CharField(max_length=6)                         #
    report_due_on = models.DateField()                              #
    tests_json_list = models.TextField()
    total_test_count = models.IntegerField()

    reference_doctor_name = models.CharField(max_length=20)         #
    sample_id = models.CharField(max_length=10)                     #
    created_by = models.ForeignKey(User)
    belongs_to_lab = models.ForeignKey(User,related_name='lab_owner',editable=False)
    technician_assigned = models.ForeignKey(User,related_name='technician_assigned',editable=False,null=True)  ## This will be filled later on after the Technician enters the data
    is_complete_by_technician = models.BooleanField(default=False)
    is_complete_by_doctor = models.BooleanField(default=False)
    status_by_technician_json_list = models.TextField()    ##Format {"test_id" :"Complete", "test_id":"Pending"}         ## To be filled in later
    status_by_doctor_json_list = models.TextField()        ##Format {"test_id" :"Complete", "test_id":"Pending"}                ## After technician fills the report
    verified_by_doctor = models.ForeignKey(User,related_name='doctor_verifier',editable=False,null=True)       ## After Doctor's verification
    share_count = models.IntegerField(default=0)                                      ## Later when sharing of report starts
    shared_with_json_list = models.TextField()                                        ## Name list of doctors shared with, these doctors will pe temporary users
    results_field = models.TextField()
