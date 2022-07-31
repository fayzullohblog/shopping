from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ProfileModel(models.Model):
    order=models.CharField(max_length=50)
    create_date=models.DateTimeField(auto_now=True)
    telephone=models.CharField(max_length=20)
    zipcode=models.IntegerField()
    
    def __str__(self):
        return self.order
   

class UserTypeModel(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title


class UserModel(AbstractUser):
    
    
    def __str__(self):
        return self.username

    USERNAME_FIELD='username'
    REQUIRED_FIELDS= ['email']












