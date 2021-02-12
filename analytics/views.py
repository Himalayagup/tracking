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
# Create your views here.


class ObjectViewedList(ListView):

    # specify the model for list view
    model = ObjectViewed


class ObjectLeadList(ListView):

    # specify the model for list view
    model = ObjectLead


@method_decorator([login_required, publisher_required], name='dispatch')
class CampaignIndividaulList(ListView):
    # specify the model for list view
    model = CampaignToPublisher
    template_name = 'analytics/campaign_indi_list.html'

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
                        self).get_context_data(*args, **kwargs)
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
        return context


class RunningCampaignsReportDetail(DetailView):
    model = Campaign
    template_name = 'analytics/campaign_detail.html'

    def get_context_data(self, *args, **kwargs):
        contenttype_obj = ContentType.objects.get_for_model(campaign_object)
        self.object = self.get_object()
        context = super(RunningCampaignsReportDetail,
                        self).get_context_data(**kwargs)
        context['click'] = ObjectViewed.objects.filter(
            object_id=self.object.campaign_key, content_type=contenttype_obj)
        context['lead'] = ObjectLead.objects.filter(
            campaign=self.get_object().campaign_name)
        return context
