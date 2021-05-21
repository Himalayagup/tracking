from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from accounts.decorators import manager_or_owner_required, owner_required

from .models import Advertiser

# Create your views here.


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AdvertiserCreate(CreateView):

    # specify the model for create view
    model = Advertiser

    # specify the fields to be displayed

    fields = ["agency",
              "company_name",
              "first_name",
              "last_name",
              "email",
              "advertiser_category",
              "status",
              ]


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AdvertiserList(ListView):

    # specify the model for list view
    model = Advertiser


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AdvertiserUpdateView(UpdateView):
    # specify the model you want to use
    template_name = "advertiser/advertiser_update_form.html"
    model = Advertiser

    # specify the fields
    fields = ["agency",
              "company_name",
              "first_name",
              "last_name",
              "email",
              "advertiser_category",
              "status",
              ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/advertiser"


@method_decorator([login_required, owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class AdvertiserDeleteView(DeleteView):
    # specify the model you want to use
    model = Advertiser

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/advertiser"
