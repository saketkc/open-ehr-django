from django import forms
from open-ehr.labs.models import PatientInfo
from open-ehr.registration.forms import *
from open-ehr.report_manager.models import *
from django.forms.widgets import CheckboxSelectMultiple
class PatientInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.created_by = kwargs.pop('created_by',None)
        self.tests_json_list = kwargs.pop('tests_json_list',None)
        self.total_test_count = kwargs.pop('total_test_count',None)
        self.belongs_to_lab = kwargs.pop('belongs_to_lab',None)
        self.status_by_technician_json_list = kwargs.pop('status_by_technician_json_list',None)
        self.results_field = kwargs.pop('results_field',None)
        self.status_by_doctor_json_list = kwargs.pop('status_by_doctor_json_list',None)
        


        super(PatientInfoForm, self).__init__(*args, **kwargs)
        self.fields['gender'] = forms.ChoiceField(choices= (('male',('Male')),('female',('Female'))))
        self.fields['patient_first_name'].label="Patient's First Name:"
        self.fields['patient_last_name'].label="Patient's Last Name:"
        self.fields['patient_dob'].label="Date of Birth:"
        self.fields['report_due_on'].label="Report due on:"
        self.fields['reference_doctor_name'].label="Reference Doctor Name:"
        self.fields['sample_id'].label="Sample Id:"
        #report_element_categories = ReportElementCategories.objects.all()
        #category_choices = ( (x.id,x.report_element_category_name) for x in report_element_categories)

        #self.fields['tests_list'] = forms.MultipleChoiceField(widget=CheckboxSelectMultiple,choices=category_choices,label=("Tests to be done"))#(required=True,widget=CheckboxSelectMultiple, choices=category_choices,label=("Tests to be done"))
        self.fields['tests_list-'+str(1)] = forms.CharField(widget=forms.TextInput(),label=("Test Name "+str(1)))
        for i in range(2,6):
            self.fields['tests_list-'+str(i)] = forms.CharField(widget=forms.TextInput(),label=("Test Name "+str(i)),required=False)


    def save(self, commit=True):
        instance = super(PatientInfoForm, self).save(commit=False)
        if self.created_by:
            instance.created_by = self.created_by
        if self.tests_json_list:
            instance.tests_json_list = self.tests_json_list
        if self.total_test_count:
            instance.total_test_count = self.total_test_count
        if self.belongs_to_lab:
            instance.belongs_to_lab = self.belongs_to_lab
        if self.status_by_doctor_json_list:
            instance.status_by_doctor_json_list = self.status_by_doctor_json_list
        if self.status_by_technician_json_list:
            instance.status_by_technician_json_list = self.status_by_technician_json_list
        if self.results_field:
            instance.results_field = self.results_field
        instance.save()
    class Meta:
        model = PatientInfo
        exclude =('tests_json_list','created_by','technician_assigned','is_complete_by_technician','is_complete_by_doctor', 'total_test_count','status_by_technician_json_list','status_by_doctor_json_list','is_verified_by_doctor','verified_by_doctor','share_count','shared_with_json_list','results_field')

class PatientResultsForm(PatientInfoForm):
    def __init__(self,*args,**kwargs):
        super(PatientResultsForm, self).__init__(*args, **kwargs)
        del self.fields['tests_list']

def render_patient_result_form(test_name_fields,report_id):

    attrs_dict ={}
    attrs_dict["readonly"]=True
    attrs_dict["value"] = report_id
    attrs_dict["required"] = True
    fields={"report_id":forms.CharField(widget=forms.TextInput(attrs=attrs_dict),required=True)}
    for test_id in test_name_fields:
        fields[test_name_fields[test_id]] = forms.CharField(widget= TextInput({ "required": "True","class": "test_input_field" }),required=True)
    return type('PatientResultsForm', (forms.BaseForm,), { 'base_fields': fields })

def render_patient_completed_form(test_name_fields,test_name_values,report_id,test_number):
    attrs_dict ={}
    attrs_dict["readonly"]=True
    attrs_dict["value"] = report_id
    attrs_dict["required"] = True
    fields={"report_id":forms.CharField(widget=forms.TextInput(attrs=attrs_dict),required=True)}
    for test_id in test_name_fields:
        fields[test_name_fields[test_id]] = forms.CharField(widget= TextInput(attrs=attrs_dict),required=True)
    return type('PatientResultsForm', (forms.BaseForm,), { 'base_fields': fields })
