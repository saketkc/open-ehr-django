from django import forms
"""
HTML5 input widgets.
TODO: Date widgets
"""
from django.forms.widgets import Input

class HTML5Input(Input):
    use_autofocus_fallback = False

    def render(self, *args, **kwargs):
        rendered_string = super(HTML5Input, self).render(*args, **kwargs)
        # js only works when an id is set
        if self.use_autofocus_fallback and kwargs.has_key('attrs') and kwargs['attrs'].get("id",False) and kwargs['attrs'].has_key("autofocus"):
            rendered_string += """<script>
if (!("autofocus" in document.createElement("input"))) {
  document.getElementById("%s").focus();
}
</script>""" % kwargs['attrs']['id']
        return rendered_string

class TextInput(HTML5Input):
    input_type = 'text'

class EmailInput(HTML5Input):
    input_type = 'email'
    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.update(dict(autocorrect='off',
                          autocapitalize='off',
                          spellcheck='false'))
        return super(EmailInput, self).render(name, value, attrs=attrs)

class TelephoneInput(HTML5Input):
    input_type = 'tel'


class URLInput(HTML5Input):
    input_type = 'url'

class SearchInput(HTML5Input):
    input_type = 'search'

class ColorInput(HTML5Input):
    """
    Not supported by any browsers at this time (Jan. 2010).
    """
    input_type = 'color'

class NumberInput(HTML5Input):
    input_type = 'number'

class RangeInput(NumberInput):
    input_type = 'range'

class DateInput(HTML5Input):
    input_type = 'date'

class MonthInput(HTML5Input):
    input_type = 'month'

class WeekInput(HTML5Input):
    input_type = 'week'

class TimeInput(HTML5Input):
    input_type = 'time'

class DateTimeInput(HTML5Input):
    input_type = 'datetime'

class DateTimeLocalInput(HTML5Input):
    input_type = 'datetime-local'
class LabRegistrationForm(forms.Form):
    lab_name = forms.CharField(required=True,widget=TextInput({ "placeholder": "First Name" }),max_length=10)
    lab_password = forms.CharField(required=True,widget=forms.PasswordInput({"placeholder": "Password","required":""}),min_length=6)

    lab_confirm_password = forms.CharField(required=True,widget=forms.PasswordInput({"placeholder": "Confirm Password","required":""}),min_length=6)
    lab_email = forms.EmailField(required=True,widget=EmailInput({ "required":"","placeholder": "user@example.com", "pattern":"^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$" }),max_length=40)
    #lab_name = forms.CharField(required=True,widget=TextInput({ "placeholder": "Last Name" }),max_length=20)

        #dateofbirth = forms.CharField(label="Date of Birth",required=True,widget=TextInput({ "required":"","placeholder": "DOB(dd/mm/yy)" }))
    #user_mobile = forms.CharField(required=True,widget=TelephoneInput({ "placeholder": "987654321" }),max_length=11)
    #email_verified_status=forms.CharField(required=False)
        #email_verification_token=forms.CharField(required=False)
class LabLoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput({ "placeholder": "", "required":"true" }),max_length=20,label="Email/Mobile No:")
    password = forms.CharField(required=True,widget=forms.PasswordInput({ "placeholder": "", "required":"true" }),max_length=11, label="Password:")


"""
Forms and validation code for user registration.

"""


from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'required':'','placeholder':''}


class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Mobile No."),
                                error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})
    attrs_dict['placeholder']=''
    attrs_dict['pattern'] = "^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$"
    email = forms.CharField(widget=EmailInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("E-mail:"))

    attrs_dict.pop("pattern")
    attrs_dict['placeholder'] = ""
    first_name = forms.CharField(widget=TextInput(attrs=dict(attrs_dict,
                                                               maxlength=15)))
    last_name = forms.CharField(widget=TextInput(attrs=dict(attrs_dict,
                                                               maxlength=15)))

    attrs_dict['placeholder']=''
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password:"))
    attrs_dict['placeholder']=''
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password (again):"))
    dateofbirth = forms.CharField(widget=TextInput(attrs=attrs_dict), label=_("Date of Birth"))                            

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']

        raise forms.ValidationError(_("A user with that username already exists."))

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                self._errors['password'] = 'Passwords must match.'
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data


    
class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.

    """
    def __init__(self,*args,**kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].label = "Lab Name"
        del(self.fields["last_name"])
        del(self.fields["dateofbirth"])
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            self._errors['email'] = 'Email in use'
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class PatientRegistrationForm(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.

    """
     #username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30, widget=forms.TextInput(attrs=attrs_dict),label=_("Mobile No."),error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})

    def __init__(self,*args,**kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['first_name', 'last_name','username','email','dateofbirth']
        self.fields.insert(5,'pin',forms.CharField(widget=TextInput(attrs=attrs_dict), label=_("Pin")))
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
       # del(self.fields["password"])
       # del(self.fields["password_confirm"])


    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            self._errors['email'] = 'Email in use'
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.

    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.

    """
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.

        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']


class ForgotPasswordForm(RegistrationForm):
    def __init__(self,*args,**kwargs):
        super(ForgotPasswordForm, self).__init__(*args, **kwargs)
        #self.fields['password'].initial = "New Password"
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['first_name'].widget.attrs['readonly'] = True
        
        

        self.fields['password_confirm'].label = "Dont Forget this time !"

class PinLoginForm(forms.Form):
    mobile_no = forms.CharField(widget=TextInput(),label=_("Mobile No."))
    date_of_birth = forms.CharField(widget=TextInput(),label=_("Date of Birth"))
    pin = forms.CharField(widget=TextInput(),label=_("Enter Pin"))
