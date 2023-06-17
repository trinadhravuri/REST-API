from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """ User profile manager that handle User fileds """
    def create_user(self,email, name, password=None):
        """ creating the user profile with parameters"""
        if not email:
            raise ValueError("user must have an email address ")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using = self._db)

        return user



    def create_superuser(self, email,name,password):
        """ Creating and save new superuser with given details """
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """ Return String Representation of the user name """
        return self.name
    
    def get_name(self):
        """ retrieving the name of User """
        return self.name