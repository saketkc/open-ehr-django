from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from open-ehr.labs.forms import PatientInfoForm,PatientResultsForm,render_patient_result_form
from open-ehr.labs.models import PatientInfo
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from open-ehr.accounts.models import UserProfile
from django.conf import settings
from django.contrib.auth.models import User
from open-ehr.registration.models import *
from open-ehr.labs.models import PatientInfo
from django.utils import simplejson
from open-ehr.report_manager.models import *
from django.utils import simplejson
@login_required
def view(request):
    belongs_to_lab = request.user.get_profile().belongs_to_lab
    if str(request.user.groups.all()[0])=="lab_doctors":
        patient_info_form = PatientInfoForm(instance=PatientInfo(),created_by=request.user,tests_json_list=[],status_by_doctor_json_list=[],status_by_technician_json_list=[])
        kwargs={"belongs_to_lab":belongs_to_lab}
        all_reports_submitted_to_doctor = PatientInfo.objects.filter(**kwargs)
        all_pending_reports = {}
        all_error_reports = {}
        all_verified_reports = {}
        i=0
        j=0
        k=0
        for report in all_reports_submitted_to_doctor:
            status_by_doctor = eval(report.status_by_doctor_json_list)
            status_by_technician = eval(report.status_by_technician_json_list)
            for test_id in status_by_doctor:
                test_name = ReportElementCategories.objects.get(pk=test_id).report_element_category_name                
                patient_full_name = str(report.patient_first_name)+"  "+ str(report.patient_last_name)
                    

                if status_by_doctor[test_id] == "pending" and status_by_technician[test_id]!="pending":
                    
                    all_pending_reports[i]=[i%2,report.report_due_on,test_name,patient_full_name,report.patient_mobile,"report-id-"+str(report.id),test_id,report.id]
                    i=i+1
                elif status_by_doctor[test_id] == "error" and status_by_technician[test_id]!="pending":
                    #test_name = ReportElementCategories.objects.get(pk=report.id).report_element_category_name
                    #patient_full_name = str(report.patient_first_name)+str(report.patient_last_name)
                    all_error_reports[j] = [j%2,report.report_due_on,test_name,patient_full_name,report.patient_mobile,report.id,test_id]
                    j= j+1
                elif status_by_doctor[test_id]== "verified" and status_by_technician[test_id]!="pending":
                    #test_name = ReportElementCategories.objects.get(pk=report.id).report_element_category_name
                    #patient_full_name = str(report.patient_first_name)+str(report.patient_last_name)
                    all_verified_reports[k] = [k%2,report.report_due_on,test_name,patient_full_name,report.patient_mobile,report.id,test_id]
                    k=k+1

        return render_to_response("labs/view.html",{"patient_info_form":patient_info_form,"pending_reports":all_pending_reports,"all_error_reports":all_error_reports,"all_verified_reports":all_verified_reports,"rangeleni":i,"rangelenj":j,"rangelenk":k},context_instance=RequestContext(request))

    elif str(request.user.groups.all()[0])=="lab_technicians":
        patient_info_form = PatientInfoForm(instance=PatientInfo(),created_by=request.user,tests_json_list=[],status_by_doctor_json_list=[],status_by_technician_json_list=[])
        
        kwargs ={"belongs_to_lab":belongs_to_lab,"is_complete_by_technician":0}
        pending_reports = PatientInfo.objects.filter(**kwargs)
        i=0
        j=0
        test_names=[]
        all_data = {}
        error_data = {}
        for report in pending_reports:
            list_of_test_categories =  eval((report.status_by_technician_json_list))
            for key in list_of_test_categories:
                test_name = ReportElementCategories.objects.get(pk=key).report_element_category_name
                if list_of_test_categories[key] == "pending":                    
                    all_data[i]=[i%2,report.report_due_on,test_name,str(report.patient_first_name)+" " + str(report.patient_last_name),report.patient_mobile,report.id,key]
                    i=i+1
                elif list_of_test_categories[key] == "error":
                    error_data[j]=[j%2,report.report_due_on,test_name,str(report.patient_first_name)+" " + str(report.patient_last_name),report.patient_mobile,report.id,key]
                    j=j+1
                
            list_of_tests = simplejson.loads(report.tests_json_list)
        #print i,j
        return render_to_response("labs/technician.html",{"all_data":all_data,"error_data":error_data,"rangelenall":i,"ranglenerror":j},context_instance=RequestContext(request))

    else :
        return HttpResponse("Waiting")


def add(request):
    instance = PatientInfo()
    post_data = request.POST.copy()
    tests_json_list = []
    i=1
    for i in range(1,6):
        test_name = post_data["tests_list-"+str(i)]
        if test_name!="":
            test_id = ReportElementCategories.objects.get(report_element_category_name=str(test_name)).id
            tests_json_list.append(int(test_id))
        else:
            break
    lab = request.user.get_profile().belongs_to_lab
    patient_mobile = str(post_data.getlist('patient_mobile')[0])
    patient_dob = str(post_data['patient_dob'])
    patient_email = str(post_data['patient_email'])
    patient_first_name = str(post_data['patient_first_name'])
    patient_last_name = str(post_data['patient_last_name'])
    status_by_doctor_json_list = {str(test_id):"not_received" for test_id in tests_json_list}
    status_by_technician_json_list = {str(test_id):"pending" for test_id in tests_json_list}
    results_field = {str(test_id):"" for test_id in tests_json_list}

    patient_info_form = PatientInfoForm(data=request.POST.copy(),instance=PatientInfo(),created_by=request.user,tests_json_list=tests_json_list,total_test_count=i,belongs_to_lab=lab,status_by_doctor_json_list=status_by_doctor_json_list,status_by_technician_json_list=status_by_technician_json_list,results_field=results_field)

    if patient_info_form.is_valid():
        patient_info_form.save()
        try:
            patient = User.objects.get(username=str(patient_mobile))
        except User.DoesNotExist:
            new_inactive_patient = RegistrationProfile.objects.create_inactive_user(patient_mobile, patient_first_name, patient_last_name,patient_dob, patient_email, "password" , "site", settings.USER_ROLES_MAP["6"] , request.user, request.user.get_profile().belongs_to_lab,False,needs_pin_to_login=True)
            new_inactive_patient.is_active = True
            new_inactive_patient.needs_pin_to_login = True
            #print "DSADASDA"
            
            new_inactive_patient.save()
            #print new_inactive_patient.needs_pin_to_login

        return HttpResponseRedirect("/labs/view/")
    else:
        return HttpResponse("NO")
        return render_to_response("labs/view.html",{"patient_info_form":patient_info_form},context_instance=RequestContext(request))

def edit(request,report_id,test_number):
    if request.method == "GET":
        report = PatientInfo.objects.get(pk=report_id)
        #tests = eval(report.tests_json_list)
        
        array_of_element_categories = test_number
        
        tests_to_be_done={}

        #for test in array_of_element_categories:
        report_element_object = ReportElementCategories.objects.get(pk=test_number)
        report_element_category_name = report_element_object.report_element_category_name
        report_element_tests = simplejson.loads(report_element_object.report_type_list_of_test_json)
        for report_test in report_element_tests:
            tests_to_be_done[report_test]=ReportElementTests.objects.get(pk=report_test).test_name
        result_form = render_patient_result_form(tests_to_be_done,report_id)
        return render_to_response("labs/edit.html",{"patient_info_form":result_form,"report_name":report_element_category_name,"patient_info":report,"testnumber":"/labs/report_edit/"+str(test_number)+"/"},context_instance=RequestContext(request))

def report_edit(request,test_number):
    if request.method=="POST":

        post_data = request.POST.copy()
        report_id = str(post_data['report_id'])
        old_results = eval(PatientInfo.objects.get(pk=report_id).results_field)
        pending_for_technician = eval(PatientInfo.objects.get(pk=report_id).status_by_technician_json_list)
        pending_for_technician[test_number]  = 'submitted'
        pending_for_doctor = eval(PatientInfo.objects.get(pk=report_id).status_by_doctor_json_list)
        pending_for_doctor[test_number] = 'pending'
        print test_number
        for objects in post_data:
            if objects!="report_id" and objects!="csrfmiddlewaretoken":
                test_id = ReportElementTests.objects.get(test_name=objects).id
                try:
                    old_results[test_number][str(test_id)] = str(post_data[objects])
                    
                except:
                    old_results[test_number] = {str(test_id) : str(post_data[objects])}
                    
        old_data = PatientInfo.objects.filter(pk=report_id).update(results_field = old_results, status_by_technician_json_list = pending_for_technician, status_by_doctor_json_list = pending_for_doctor)
        return HttpResponseRedirect("/labs/view/")

def report_lookup(request):
    reports = ReportElementCategories.objects.filter(report_element_category_name__istartswith=request.GET[u'q'])
    
    results = "" 
    for report in reports:
        results+="\n"+str(report.report_element_category_name)
    
    
    return HttpResponse(simplejson.dumps(results),mimetype='application/json')

def view_submitted_report(request,report_id,test_number):
    if request.method  == "GET":
        report = PatientInfo.objects.get(pk=report_id)
        tests_json_list = eval(report.tests_json_list)
        tests_to_be_done={}
        #report_name = report.report_element_category_name
        list_of_result =  eval((report.results_field))
        all_data = {}
        i = 0
        report_name = ReportElementCategories.objects.get(pk=tests_json_list[0]).report_element_category_name
        for test_id in list_of_result[test_number]:
            test_name = ReportElementTests.objects.get(pk=test_id).test_name
            
            test_result_value = list_of_result[test_number][test_id]
            all_data[i] = [test_name,test_result_value]
            i = i+1
        return render_to_response("labs/view_submitted.html",{"all_data":all_data,"report_name":report_name,"patient_info":report,"rangelen":i,"report_id":report_id,"test_id":test_number},context_instance=RequestContext(request))

def confirm_submitted_report(request):
    data = request.POST.copy()
    report_id = data['report_id']
    reject = confirm = ""
    try:
        reject = data['reject']
    except:
        confirm = data['confirm']
    test_number = data['test_id']
    report = PatientInfo.objects.get(pk=report_id)
    pending_for_doctor = eval(report.status_by_doctor_json_list)
    pending_for_technician = eval(report.status_by_technician_json_list)
    if confirm:
        pending_for_doctor[test_number] = "verified"
    elif reject:
        pending_for_doctor[test_number] = "error"
        pending_for_technician[test_number] = "error"
        
    new_data = PatientInfo.objects.filter(pk=report_id).update(status_by_doctor_json_list = pending_for_doctor,status_by_technician_json_list = pending_for_technician,verified_by_doctor=request.user)
    return HttpResponseRedirect("/labs/view")

def patient_view(request):
    patient = request.user.username
    all_reports = PatientInfo.objects.filter(patient_mobile=patient)
    accepted_reports = {}
    pending_reports = {}
    i = 1
    j = 1
    for report in all_reports:
        status_from_doctor = eval(report.status_by_doctor_json_list)
        status_from_technician = eval(report.status_by_technician_json_list)
        #print status_from_doctor
        for category_id,status in status_from_doctor.iteritems():
            #print category_id
            if status=="verified":
                accepted_reports[i] = [i%2,report.report_due_on,str(ReportElementCategories.objects.get(pk=category_id).report_element_category_name),str(report.id),str(category_id),str(report.belongs_to_lab)]
                i=i+1

        for category_id,status in status_from_technician.iteritems():
            
            if status=="pending":
                pending_reports[j] = [j%2,report.report_due_on,str(ReportElementCategories.objects.get(pk=category_id).report_element_category_name),str(report.id),str(category_id),str(report.belongs_to_lab)]
                j=j+i

        for category_id,status in status_from_doctor.iteritems():
            
            if status=="pending" or status =="not_received":
                pending_reports[j] = [j%2,report.report_due_on,str(ReportElementCategories.objects.get(pk=category_id).report_element_category_name),str(report.id),str(category_id),str(report.belongs_to_lab)]
                j=j+i
        

        #print pending_reports
        #print accepted_reports

        

    return render_to_response("labs/patient.html",{"accepted_reports":accepted_reports,"pending_reports":pending_reports,"rangeleni":i,"rangelenj":j,"report_id":"id","test_id":"test_number"},context_instance=RequestContext(request))

def share(request,report_id):
    return HttpResponse("TEST")
    

def view_expanded(request,report_id,category_id):
    if request.method == "GET":
        report = PatientInfo.objects.get(pk=report_id)
        report_name  = ReportElementCategories.objects.get(pk=category_id).report_element_category_name                
        tests_json_list = eval(report.tests_json_list)
        list_of_result =  eval((report.results_field))
        #array_of_element_categories = test_number
        tests_to_be_done={}
        i=0
        print list_of_result
        #test_number = '5'
        all_data = {}
        #for category_id in list_of_result:
        for test_id in list_of_result[str(category_id)]:
            test_name = ReportElementTests.objects.get(pk=test_id).test_name
            test_result_value = list_of_result[category_id][test_id]
            all_data[i] = [test_name,test_result_value]
            i = i+1
        #for test in array_of_element_categories:
         #   report_element_object = ReportElementCategories.objects.get(pk=test)
          #  report_element_tests = simplejson.loads(report_element_object.report_type_list_of_test_json)
           # for report_test in report_element_tests:
            #    tests_to_be_done[report_test]=ReportElementTests.objects.get(pk=report_test).test_name
        #result_form = render_patient_result_form(tests_to_be_done,report_id)
        
        return render_to_response("labs/view_expanded.html",{"all_data":all_data,"rangelen":i,"report_name":report_name},context_instance=RequestContext(request))
