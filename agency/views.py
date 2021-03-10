from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import Agency
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.decorators import owner_required, manager_or_owner_required
# Create your views here.


class HomePage(TemplateView):
    template_name = 'agency/index.html'


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AgencyCreate(CreateView):

    # specify the model for create view
    model = Agency

    # specify the fields to be displayed

    fields = ["agency_name",
              "agency_address",
              "contact_person",
              "email",
              "contact_number",
              "alternate_number", ]


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AgencyList(ListView):

    # specify the model for list view
    model = Agency


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AgencyUpdateView(UpdateView):
    # specify the model you want to use
    template_name = "agency/agency_update_form.html"
    model = Agency

    # specify the fields
    fields = ["agency_name",
              "agency_address",
              "contact_person",
              "email",
              "contact_number",
              "alternate_number", ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/agency"


@method_decorator([login_required, owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AgencyDeleteView(DeleteView):
    # specify the model you want to use
    model = Agency

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/agency"
