from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import auth
from django.template import RequestContext
from open-ehr.report_manager.models import *
from open-ehr.report_manager.forms import *
from django.utils import simplejson
@user_passes_test(lambda u: u.is_superuser)
def view_all_reports(request):
    #all_reports = ReportTypes.objects.all()
    report_choice_form = ReportChoiceForm()
    instance_of_model = ReportTypes()
    new_report_type_form = NewReportTypeForm(instance=ReportTypes(),report_belongs_to_lab=request.user)
    return render_to_response("report_manager/view_reports.html",{'report_choice_form':report_choice_form,'new_report_type_form':new_report_type_form},context_instance=RequestContext(request))

def add_new_report_type(request):
    if request.method=='POST':
        new_report = ReportTypes()
        new_report_type_form = NewReportTypeForm(data=request.POST,instance=new_report,report_belongs_to_lab=request.user) #ReportTypes()
        if new_report_type_form.is_valid():
            new_report_type_form.save()
            return HttpResponse("Done")
        else :
            return HttpResponse("Ditch")
def render_testelement_categories_form(request):
    if request.method == "GET":

        report_id = request.GET.get('report_name','')
        report_object = ReportTypes.objects.get(pk=report_id)
        array_of_element_categories = simplejson.loads(report_object.report_element_json_list)
        tests_to_be_done = {}
        for test in array_of_element_categories:
            report_element_object = ReportElementCategories.objects.get(pk=test)
            report_element_tests = simplejson.loads(report_element_object.report_type_list_of_test_json)

            for report_test in report_element_tests:
                tests_to_be_done[report_test]=ReportElementTests.objects.get(pk=report_test).test_name


        result_form = report_result_form(tests_to_be_done)
        request.session["list_of_tests"]=tests_to_be_done
        request.session['report_id'] = report_id
        report_choice_form = ReportChoiceForm()
        instance_of_model = ReportTypes()
        new_report_type_form = NewReportTypeForm(instance=ReportTypes(),report_belongs_to_lab=request.user)
        return render_to_response("report_manager/result_reports.html",{'report_choice_form':report_choice_form,'new_report_type_form':new_report_type_form,'results_form':result_form},context_instance=RequestContext(request))
    else:
        list_of_tests = request.session["list_of_tests"]
        post_data = request.POST.copy()
        report_id = request.session['report_id']
        post_data["report_type"]=report_id
        post_data["result_field"]=""
        for test_id in list_of_tests:
            post_data["result_field"]+=post_data[list_of_tests[test_id]]
            del post_data[list_of_tests[test_id]]
        results_report = ReportResults()
        report = ReportTypes.objects.get(id=report_id)
        results_form = ReportResultsForm(data=post_data,instance=results_report,lab_owner=request.user,report_type=report) #ReportTypes()
        if results_form.is_valid():
            results_form.save()
            ReportResults.objects.create_inactive_patient(post_data["user_mobile"],post_data["user_dob"],request.user)
        else:
            return HttpResponse("ERROR")
        return HttpResponse("DOne")
