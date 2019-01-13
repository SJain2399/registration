from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.validators import MinLengthValidator

# Create your models here.
    
class userinfo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    #additional fields
    
    phone = PhoneField(blank=True, help_text='Contact phone number',unique=True)
    aadharnumber=models.IntegerField()
    address=models.CharField(max_length=200, blank=True, null=True)
    gender=gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default= 'M')

    def __str__(self):
        return self.user.username        
