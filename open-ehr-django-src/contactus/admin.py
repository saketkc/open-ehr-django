from django.contrib import admin
from open-ehr.contactus.models import UserEmail
class EmailAdmin(admin.ModelAdmin):
    list_display=['email']#,'email_verified_status','email_verification_token']
    search_fields=['email']
admin.site.register(UserEmail,EmailAdmin)
