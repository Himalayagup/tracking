from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView)
from .models import ObjectViewed, ObjectLead
from campaign.models import Campaign, CampaignToPublisher
from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.decorators import owner_required, publisher_required, manager_or_owner_required
from django.db.models import Q
from .filters import CampaignIndividaulFilter, ClickViewFilter, LeadFilter, ClickIndiFilter, LeadIndiFilter
from django.db.models import Count
# To export csv
import csv

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class ObjectViewedList(ListView):

    # specify the model for list view
    model = ObjectViewed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ClickViewFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class ObjectViewedDetail(DetailView):

    # specify the model for list view
    model = ObjectViewed


class ObjectLeadList(ListView):

    # specify the model for list view
    model = ObjectLead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = LeadFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


@method_decorator([login_required, publisher_required], name='dispatch')
class CampaignIndividaulList(ListView):
    # specify the model for list view
    model = CampaignToPublisher
    template_name = 'analytics/campaign_indi_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CampaignIndividaulFilter(
            self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.Publisher_User)


@method_decorator([login_required], name='dispatch')
class CampaignDataIndiDetail(DetailView):
    model = Campaign
    template_name = 'publisher/publisher_campaign_detail.html'

    def get_context_data(self, *args, **kwargs):
        val_filter1 = Q(
            try_new__campaign=self.get_object().campaign_key)
        val_filter2 = Q(
            try_new__user=self.request.user.Publisher_User
        )
        self.object = self.get_object()
        context = super(CampaignDataIndiDetail,
                        self).get_context_data(**kwargs)
        context['lead'] = ObjectLead.objects.filter(
            campaign=self.get_object().campaign_name, publisher=self.request.user.Publisher_User.company_name)
        context['click'] = ObjectViewed.objects.filter(
            val_filter1).filter(val_filter2)

        return context


class CampaignWiseReport(ListView):
    model = Campaign
    template_name = 'analytics/campaign_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CampaignWiseReport,
                        self).get_context_data(**kwargs)
        context['click'] = ObjectViewed.objects.all()
        context['lead'] = ObjectLead.objects.all()
        # for lead data
        dict_lead = {}
        for campaign in Campaign.objects.all():
            lead_data = ObjectLead.objects.filter(
                campaign=campaign.campaign_name).count()
            dict_lead[campaign.campaign_name] = lead_data
            context['lead_data'] = (dict_lead.items())
        # for click data
        dict_click = {}
        for campaign in Campaign.objects.all():
            val_filter = Q(
                try_new__campaign=campaign.campaign_key)
            click_data = ObjectViewed.objects.all().filter(
                val_filter).count()
            dict_click[campaign.campaign_name] = click_data
            context['click_data'] = sorted(dict_click.items())
        return context


class RunningCampaignsReportDetail(DetailView):
    model = Campaign
    template_name = 'analytics/campaign_detail.html'

    def get_context_data(self, *args, **kwargs):
        val_filter1 = Q(
            try_new__campaign=self.get_object().campaign_key)
        context = super(RunningCampaignsReportDetail,
                        self).get_context_data(**kwargs)
        self.request.session['campaign_detail'] = self.object.campaign_name

        context['click'] = ObjectViewed.objects.all().filter(
            val_filter1)
        a = ObjectLead.objects.filter(
            campaign=self.get_object().campaign_name)
        data_ne = self.get_object().publisher_campaign.all()
        # for lead data
        dict_lead = {}
        for lead_i in data_ne:
            lead_data = ObjectLead.objects.filter(
                campaign=self.get_object().campaign_name).filter(publisher=lead_i.company_name).count()
            dict_lead[lead_i.company_name] = lead_data
        context['lead_data'] = (dict_lead.items())
        # for click data
        dict_click = {}
        for click_i in data_ne:
            val_filter3 = Q(
                try_new__user=click_i.pk)
            click_data = ObjectViewed.objects.all().filter(
                val_filter1).filter(val_filter3).count()
            dict_click[click_i.company_name] = click_data
            context['click_data'] = (dict_click.items())
        return context
