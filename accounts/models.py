from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.
STATUS = (
    ("pending", "Pending"),
    ("active", "Active"),
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
)


class User(AbstractUser):
    is_publisher = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField("Gender",
                              help_text="Choose gender",
                              max_length=22,
                              choices=GENDER, default=GENDER[0][0])


class Publisher(models.Model):
    user_name = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="Publisher_User")
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    status = models.CharField("Status",
                              help_text="Choose the publisher status",
                              max_length=22,
                              choices=STATUS, default=STATUS[0][0])

    def __str__(self):
        return "%s | %s" % (self.company_name, self.user_name.first_name)


class Manager(models.Model):
    user_name = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="Manager_User")
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    status = models.CharField("Status",
                              help_text="Choose the publisher status",
                              max_length=22,
                              choices=STATUS, default=STATUS[0][0])

    def __str__(self):
        return self.user_name.first_name


class Owner(models.Model):
    user_name = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="Owner_User")
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.user_name.first_name
