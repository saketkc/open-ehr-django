from django import forms
from open-ehr.registration.forms import *
from open-ehr.accounts.models import password_generator
class UserRegistrationForm(RegistrationFormUniqueEmail):
    def __init__(self,*args, **kwargs ):
        super(UserRegistrationForm,self).__init__(*args,**kwargs)
        del self.fields['first_name']
        CHOICES = (('3', 'Doctor',), ('4', 'Technician'), ('5','Receptionist'))
        self.fields['first_name'] = forms.CharField(widget=TextInput(),label=("First Name"))
        self.fields['last_name'] = forms.CharField(widget=TextInput(),label=("Last Name"))
        self.fields['username'] = forms.CharField(widget=TextInput(),label=("User Name"))
        attrs_dict={"value":password_generator()}
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=("Password"))
        self.fields['password_confirm'] = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=("Confirm Password"))
        self.fields['user_role'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=("User Role"))
