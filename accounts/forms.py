from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from accounts.models import User, Publisher, Manager, Owner

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
)


class PublisherSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=GENDER)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_publisher = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        publisher = Publisher.objects.create(user_name=user)
        publisher.company_name = self.cleaned_data.get('company_name')
        publisher.email = self.cleaned_data.get('email')
        publisher.save()
        return user


class ManagerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=GENDER)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.is_staff = False
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        manager = Manager.objects.create(user_name=user)
        manager.mobile = self.cleaned_data.get('mobile')
        manager.email = self.cleaned_data.get('email')
        manager.save()
        return user


class OwnerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=GENDER)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner = True
        user.is_staff = True
        user.is_superuser = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        owner = Owner.objects.create(user_name=user)
        owner.mobile = self.cleaned_data.get('mobile')
        owner.email = self.cleaned_data.get('email')
        owner.save()
        return user
