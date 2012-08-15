from django.db import models
#admin.autodiscover()
class UserEmail(models.Model):

    email=models.EmailField()
    email_verfied_status=models.CharField(max_length=1)
    email_verification_token=models.CharField(max_length=100)

# Create your models here.
