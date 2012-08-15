from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404

from django.shortcuts import redirect
from open-ehr.registration.models import *
from open-ehr.registration.forms import *
from open-ehr.accounts.models import UserProfile
from django.contrib import auth
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.messages import get_messages
from django.contrib.auth import logout
import hashlib
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            user_exists = User.objects.get(username=username)
        except:
            messages.error(request, 'User Does Not Exist')
            return HttpResponseRedirect(reverse('register_lab'))
        user_is_new_patient = User.objects.get(username=username).get_profile().needs_pin_to_login
        #if user_is_new_patient:
            #messages.error(request, 'Pin not Activated Yet')
            #return HttpResponseRedirect(reverse('register_lab'))
            
            
        
        
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Wrong password')
            return HttpResponseRedirect(reverse('register_lab'))               
        
        elif not user.is_active:
            messages.error(request, 'User Not Activated')
            return HttpResponseRedirect(reverse('register_lab'))
        
        else:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            user_groups = user.groups.all()
            #print user_groups[0]

            if (str(user_groups[0])=="lab_super_users")or (str(user_groups[0])=="open-ehr_super_users"):
                return HttpResponseRedirect("/accounts/view/")
            elif (str(user_groups[0])=="lab_doctors") or (str(user_groups[0])=="lab_technicians"):
                return HttpResponseRedirect("/labs/view/")
            else:
                return HttpResponseRedirect("/labs/patient/view/")
    #except:
            #messages.error(request, 'User Notf Activated')
            #return HttpResponseRedirect(reverse('register_lab'))
            
        
        
        
            
                
    else:
        return HttpResponseRedirect("/register/")

def register_lab(request,template_name):
    if request.method == 'POST':
        request_post = request.POST
        lab_registration_form = PatientRegistrationForm(request_post)
        login_form = LabLoginForm()
        hashstring=hashlib.sha1(str(request.POST.get('csrf_token')))
        if request.session.get('sesionform')!=hashstring:
            if lab_registration_form.is_valid():
                username = lab_registration_form.cleaned_data['username']
                first_name = lab_registration_form.cleaned_data['first_name']
                
                email = lab_registration_form.cleaned_data['email']
                password = "health" #lab_registration_form.cleaned_data['password']
                last_name = lab_registration_form.cleaned_data['last_name']
                group = "lab_patients_registered"
                created_by = User.objects.get(pk=1)
                new_user = RegistrationProfile.objects.create_inactive_user(username, first_name, last_name, '1000-01-01' ,email, password, "site", group, created_by )
                messages.success(request, 'An Email Has been sent !' )
                return HttpResponseRedirect(reverse('register_lab'))
            else:
                messages.error(request,"The form wasn't valid!")
                return render_to_response('registration/patient_login.html',
                        {'patient_registration_form': lab_registration_form,'login_form':login_form,'messages':get_messages(request)})
        else:
            return HttpResponseRedirect(reverse('register_lab'))
            #return redirect("/register")
    else:
        lab_registration_form =  PatientRegistrationForm()
        pin_login_form = PinLoginForm()
        login_form = LabLoginForm()
        return render_to_response('registration/patient_login.html', {'patient_registration_form':lab_registration_form,'login_form':login_form,'pin_login_form':pin_login_form,'messages':get_messages(request)})

def labs(request):
    login_form = LabLoginForm()
    return render_to_response('registration/labs_login.html',{'login_form':login_form,'messages':get_messages(request)})
    
def activate_lab(request,activation_key):
    registered = RegistrationProfile.objects.activate_user(activation_key)
    lab_registration_form = RegistrationFormUniqueEmail()
    login_form = LabLoginForm()
    if registered:
        messages.success( request, 'Account Activated. Login To Continue.' )
        return HttpResponseRedirect(reverse('register_lab'))

    else:
        messages.success( request, 'There was a problem activating' )
        return HttpResponseRedirect(reverse('register_lab'))

def accounts(request,username):
    templates = {"lab_super_user" : "lab_super_user_page.html","lab_technician" : "lab_technician_page.html", "patient" :"patient_page.html"}
    #user_profile = UserProfile.objects.get(user=request.user)
    #print user_profile.is_technician
    if request.user.is_superuser:
        return HttpResponse("ETE")

    else:
        return HttpResponse("NO")


def new_key():
    while True:
        key = User.objects.make_random_password(70)
        try:
            LostPassword.objects.get(key=key)
        except LostPassword.DoesNotExist:
            return key

def forgotpassword(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            lostpassword = LostPassword.objects.create(user=user,key=new_key())
            message = 'http://%s:%s/change/%s/' % (
                request.META['SERVER_NAME'],
                request.META['SERVER_PORT'],
                lostpassword.key)
        except User.DoesNotExist:
            message = 'Unknown user'
    else:
        message = ''

    return render_to_response('registration/forgot_password.html',{'message': message})

def change_password(request, key):
    
    lostpassword = get_object_or_404(LostPassword, key=key)

    if lostpassword.is_expired():
        lostpassword.delete()
        message = 'Page expired'
    else:
        user=User.objects.get(username=lostpassword.user.username)
        forgot_password_form = ForgotPasswordForm(initial={'username': user.username,'first_name':user.first_name,'email':user.email})
          
        
        

    return render_to_response('registration/new_password.html',{'forgot_password_form': forgot_password_form})

def updatepassword(request):
    if request.method=="POST":
        info = request.POST.copy()
        user = User.objects.get(username=info['username'])
        if info['password']!=info['password_confirm']:
            return HttpResponse("Passwords don't match")
        else:
            #user.password=info['password']
            print user.password
            print info['password']
            print user.password
            user.set_password(info['password'])
            print user.password
            user.save()
            return HttpResponse("DA")

def pinlogin(request):
    if request.method=="POST":
        username = request.POST['mobile_no']
        date_of_birth = request.POST['date_of_birth']
        pin = request.POST['pin']
        first_name = username
        last_name = username
        email = "TEST@TEST.cc"
        password = "health"
        group = "lab_patients_unregistered"
        created_by = User.objects.get(username="saketkc")
        new_user = RegistrationProfile.objects.create_inactive_user(username, first_name, last_name, date_of_birth ,email, password, "site", group, created_by=created_by, lab_owner="self" , send_email=False,needs_pin_to_login=True)
        if pin =="rest":
            return HttpResponse("DONE")
def logout_view(request):
        logout(request)
        messages.success(request,'Logged out Successfully')
        return HttpResponseRedirect("/register")
