from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
 

user_gender_choices = [('Male','Male'),('Female','Female'),('Other','Other')]
user_type_choices = [('Primary','Primary'),('Secondary','Secondary')]

class User(AbstractUser):
    email = models.EmailField(max_length=250,unique=True)
    first_name = models.CharField(max_length=80, default=0)
    last_name = models.CharField(max_length=80, default=0)
    User_ID = models.AutoField(primary_key=True)
    address = models.CharField(max_length=250, blank=True,null=True)
    session_token = models.CharField(max_length=20, default=0)
    phone = models.CharField(unique=True,max_length=20)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10,choices=user_gender_choices default=0)
    Type = models.CharField(max_length=10,choices=user_type_choices default=0)
    password = models.CharField(max_length=100,null=True,blank=True)
    # standard
