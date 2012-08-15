from django import forms
from open-ehr.report_manager.models import *
class NewReportTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.report_belongs_to_lab = kwargs.pop('report_belongs_to_lab', None)
        super(NewReportTypeForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(NewReportTypeForm, self).save(commit=False)
        if self.report_belongs_to_lab:
            instance.report_belongs_to_lab = self.report_belongs_to_lab
        return instance.save()

    class Meta:
        model = ReportTypes
        exclude = ('report_belongs_to_lab')
class  ReportChoiceForm(forms.Form):
    report_name = forms.ModelChoiceField(queryset = ReportTypes.objects.all())

class ReportResultsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.lab_owner = kwargs.pop('lab_owner',None)
        self.report_type =  kwargs.pop('report_type',None)
        super(ReportResultsForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ReportResultsForm, self).save(commit=False)
        if self.lab_owner:
            instance.lab_owner = self.lab_owner
        if self.report_type:
            instance.report_type = self.report_type
        instance.save()
    class Meta:
        model = ReportResults
        exclude =('lab_owner','report_type')

def report_result_form(test_name_fields):
    fields = {'user_mobile' : forms.CharField(max_length=11),"user_dob":forms.CharField(),}
    for test_id in test_name_fields:
        fields[test_name_fields[test_id]] = forms.CharField(max_length=100)
    return type('ReportResultsForm', (forms.BaseForm,), { 'base_fields': fields })
