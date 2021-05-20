
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  RedirectView, TemplateView, UpdateView)
from hitcount.views import HitCountDetailView

from accounts.decorators import manager_or_owner_required, owner_required
from analytics.filters import CampaignIndividaulFilter
from analytics.mixins import ObjectViewMixin

from .filters import CampaignStatusFilter
from .models import Campaign, CampaignToPublisher

# Create your views here.


class HomePage(TemplateView):
    template_name = 'campaign/index.html'


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignDetail(DetailView):
    model = Campaign


# class CampaignDetail(HitCountDetailView):
#     model = Campaign
#     count_hit = True

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(xframe_options_exempt, name='dispatch')
class CampaignToPublisherDetail(ObjectViewMixin, DetailView):
    template_name = "publisher/campaigntopublisher_detail.html"
    model = CampaignToPublisher

    def get_context_data(self, *args, **kwargs):
        context = super(CampaignToPublisherDetail,
                        self).get_context_data(*args, **kwargs)
        from analytics.models import unique_click_id
        self.request.session['publisher'] = self.object.user.company_name
        self.request.session['publisher_id'] = self.object.user.pk
        self.request.session['campaign'] = self.object.campaign.campaign_name
        self.request.session['campaign_id'] = self.object.campaign.campaign_key
        self.request.session['click_id'] = unique_click_id
        context["click_id"] = unique_click_id
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(CampaignToPublisherDetail, self).render_to_response(
            context, **response_kwargs)
        from analytics.models import unique_click_id
        response.set_cookie(
            "publisher1", self.object.user.company_name, max_age=86400, samesite='None', secure=True)
        response.set_cookie(
            "campaign1", self.object.campaign.campaign_name, max_age=86400, samesite='None', secure=True)
        response.set_cookie(
            "publisher_id1", self.object.user.pk, max_age=86400, samesite='None', secure=True)
        response.set_cookie(
            "campaign_id1", self.object.campaign.campaign_key, max_age=86400, samesite='None', secure=True)

        return response


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CampaignIndividaulFilter(
            self.request.GET, queryset=self.get_queryset())
        context['filter1'] = CampaignStatusFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


@method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
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


@method_decorator([login_required, owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignDeleteView(DeleteView):
    # specify the model you want to use
    model = Campaign

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/campaign"
