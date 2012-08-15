from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from open-ehr.accounts.models import UserProfile
from open-ehr.registration.models import RegistrationProfile
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from open-ehr.accounts.forms import *
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages

def redirectblog(request,path):
    return HttpResponseRedirect("http://blog.open-ehrhx.com/"+path)
    

@login_required
@user_passes_test(lambda u: (str(u.groups.all()[0])=="lab_super_users")) #(str(u.groups.all()[0])=="open-ehr_super_users") or
def view(request,username):
    ## No username provided. View All Users belonging to that lab mode !
    belongs_to_lab = request.user.get_profile().belongs_to_lab
    lab_name = request.user.first_name
    if username=="":


        try:
            #all_users_belonging_to_lab = User.objects.select_related('profile_cache').all()
            all_users_belonging_to_lab = UserProfile.objects.filter(created_by=request.user) #belonging_to_lab
        except:
            all_users_belonging_to_lab=[]
    else:
        try:
            all_users_belonging_to_lab = User.objects.get(username=username)
        except:
            all_users_belonging_to_lab = []

    return render_to_response("accounts/view.html",{"all_users":all_users_belonging_to_lab,"lab_name":lab_name},context_instance=RequestContext(request))

@login_required
#@user_passes_test(lambda u : ("lab_super_users" in str(u.groups.all()[0])) or ("open-ehr_super_users" in  str(u.groups.all()[0]) ))

def edit(request,username):
    return HttpResponse("OK")

def delete(request,username):
    return HttpResponse("OK")
@login_required
def add(request,username):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data['username']
            first_name = registration_form.cleaned_data['first_name']
            last_name = registration_form.cleaned_data['last_name']
            email = registration_form.cleaned_data['email']
            password = registration_form.cleaned_data['password']
            group = settings.USER_ROLES_MAP[str(registration_form.cleaned_data['user_role'])]

            new_user = RegistrationProfile.objects.create_inactive_user(username, first_name, last_name,  '1000-01-01',email, password, "site", group, request.user, request.user.get_profile().belongs_to_lab)
            messages.success(request, 'An Email Has been sent !' )
            registration_form = UserRegistrationForm()
        else:
            messages.error(request,"The form wasn't valid!")
        return render_to_response("accounts/add.html",{"registration_form":registration_form,"messages":get_messages(request)},context_instance=RequestContext(request))
    else:

        registration_form = UserRegistrationForm()
        return render_to_response("accounts/add.html",{"registration_form":registration_form},context_instance=RequestContext(request))
