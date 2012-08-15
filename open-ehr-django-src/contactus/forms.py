from django import forms
class EmailForm(forms.Form):
    email=forms.EmailField()
    email_verified_status=forms.CharField(required=False)
    email_verification_token=forms.CharField(required=False)
