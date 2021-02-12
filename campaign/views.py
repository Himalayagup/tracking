from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView)
from .models import Campaign, CampaignToPublisher
from analytics.mixins import ObjectViewMixin
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
from analytics.mixins import ObjectViewMixin

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.decorators import owner_required, manager_or_owner_required
# Create your views here.


class HomePage(TemplateView):
    template_name = 'campaign/index.html'


@method_decorator([login_required, manager_or_owner_required], name='dispatch')
class CampaignDetail(DetailView):
    model = Campaign


# class CampaignDetail(HitCountDetailView):
#     model = Campaign
#     count_hit = True

class CampaignToPublisherDetail(ObjectViewMixin, DetailView):
    template_name = "publisher/campaigntopublisher_detail.html"
    model = CampaignToPublisher

    def get_context_data(self, *args, **kwargs):
        context = super(CampaignToPublisherDetail,
                        self).get_context_data(*args, **kwargs)
        self.request.session['publisher'] = self.object.user.company_name
        self.request.session['publisher_id'] = self.object.user.pk
        self.request.session['campaign'] = self.object.campaign.campaign_name
        self.request.session['campaign_id'] = self.object.campaign.campaign_key
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(CampaignToPublisherDetail, self).render_to_response(
            context, **response_kwargs)
        response.set_cookie("publisher1", self.object.user)
        response.set_cookie("campaign1", self.object.campaign)
        response.set_cookie("publisher_id1", self.object.user.pk)
        response.set_cookie("campaign_id1", self.object.campaign.campaign_key)

        return response


@method_decorator([login_required, manager_or_owner_required], name='dispatch')
class CampaignCreate(CreateView):

    # specify the model for create view
    model = Campaign

    # specify the fields to be displayed

    fields = ["advertiser",
              "campaign_name",
              "landing_url",
              "expire_url",
              "start_date",
              "end_date",
              "campaign_type",
              "campaign_category",
              "comment",
              "status",
              # "campaign_key,"
              ]


@method_decorator([login_required], name='dispatch')
class CampaignList(ListView):

    # specify the model for list view
    model = Campaign


@method_decorator([login_required, manager_or_owner_required], name='dispatch')
class CampaignUpdateView(UpdateView):
    # specify the model you want to use
    template_name = "campaign/campaign_update_form.html"
    model = Campaign

    # specify the fields
    fields = ["advertiser",
              "campaign_name",
              "landing_url",
              "expire_url",
              "start_date",
              "end_date",
              "campaign_type",
              "campaign_category",
              "comment",
              "status",
              # "campaign_key,"
              ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/campaign"


@method_decorator([login_required, owner_required], name='dispatch')
class CampaignDeleteView(DeleteView):
    # specify the model you want to use
    model = Campaign

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/campaign"
