from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

## Password Generator
def password_generator():
    import random
    password=""
    for i in range(0,6):
        password=password+str(random.randint(0,9))

    return password

def add_user_to_group(username,groupname):
    user = User.objects.get(username=username)
    group = Group.objects.get(name=groupname)
    try:
        user.groups.add(group)
        return True
    except:
        return False


class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile_cache')
    dob = models.DateField()
    created_by = models.ForeignKey(User,related_name="created_by_doctor_or_technician")
    belongs_to_lab = models.ForeignKey(User,related_name="belongs_to_lab_id")
    is_lab_super_user = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    needs_pin_to_login = models.BooleanField(default=False)
    pin_exists = models.BooleanField(default=False)
    pin_permanent = models.CharField(max_length=6,default='null')

    def save(self):
        super(UserProfile, self).save()

class LabSuperUsers(models.Model):
    lab_id = models.CharField(max_length=10)
    lab_super_user = models.OneToOneField(User)
    lab_name = models.CharField(max_length=20)
