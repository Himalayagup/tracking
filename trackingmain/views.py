from datetime import date, datetime, time, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from accounts.models import Publisher
from analytics.models import ObjectLead, ObjectViewed
from campaign.models import Campaign, CampaignToPublisher

# today_fil = datetime.now()
today_fil = date.today()
yesterday = datetime.now() - timedelta(days=1)


@method_decorator([login_required], name='dispatch')
class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage,
                        self).get_context_data(*args, **kwargs)
        # for manager/admin
        context['publisher'] = Publisher.objects.filter(
            status="pending")
        context['campaign'] = Campaign.objects.filter(
            status="pending")
        context['campaign_request'] = CampaignToPublisher.objects.filter(
            status_cam="pending")
        context['view_today'] = ObjectViewed.objects.filter(
            timestamp__year=today_fil.year, timestamp__month=today_fil.month, timestamp__day=today_fil.day)
        context['view_yesterday'] = ObjectViewed.objects.filter(
            timestamp__year=yesterday.year, timestamp__month=yesterday.month, timestamp__day=yesterday.day)
        context['view_month'] = ObjectViewed.objects.filter(
            timestamp__year=today_fil.year, timestamp__month=today_fil.month)
        context['lead_today'] = ObjectLead.objects.filter(
            lead_timestamp__year=today_fil.year, lead_timestamp__month=today_fil.month, lead_timestamp__day=today_fil.day)
        context['lead_yesterday'] = ObjectLead.objects.filter(
            lead_timestamp__year=yesterday.year, lead_timestamp__month=yesterday.month, lead_timestamp__day=yesterday.day)
        context['lead_month'] = ObjectLead.objects.filter(
            lead_timestamp__year=today_fil.year, lead_timestamp__month=today_fil.month)

        # for publisher

        return context


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
