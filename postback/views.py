from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView

from analytics.models import ObjectLead, ObjectViewed
from analytics.utils import get_client_ip

# Create your views here.


class PostbackLead(TemplateView):
    template_name = 'postback/postback_trackinglead.html'

    def get(self, request, *args, **kwargs):
        id_data = request.GET
        if id_data:
            click_id_data = id_data['clk_id']
            click_data = ObjectViewed.objects.get(click_id=click_id_data)
            print(click_id_data)
            if click_data:
                ip_address = None
                try:
                    # get_client_ip is utility in utils.py file to store IP address
                    ip_address = get_client_ip(request)
                except:
                    pass

                old_data = ObjectLead.objects.filter(
                    campaign=click_data.content_object.campaign.campaign_name,
                    campaign_id=click_data.content_object.campaign.campaign_key,
                    publisher=click_data.content_object.user.company_name,
                    publisher_id=click_data.content_object.user.pk,
                    ip_address=ip_address)
                if old_data:
                    return HttpResponse("Duplicate Key")
                else:
                    lead_data = ObjectLead.objects.create(
                        campaign=click_data.content_object.campaign.campaign_name,
                        campaign_id=click_data.content_object.campaign.campaign_key,
                        publisher=click_data.content_object.user.company_name,
                        publisher_id=click_data.content_object.user.pk,
                        ip_address=ip_address,
                        click_id=click_id_data)

        return HttpResponse("Done")

    def post(self, request, *args, **kwargs):
        id_data = request.POST
        if id_data:
            click_id_data = id_data['clk_id']
            click_data = ObjectViewed.objects.get(click_id=click_id_data)
            print(click_id_data)
            if click_data:
                ip_address = None
                try:
                    # get_client_ip is utility in utils.py file to store IP address
                    ip_address = get_client_ip(request)
                except:
                    pass

                old_data = ObjectLead.objects.filter(
                    campaign=click_data.content_object.campaign.campaign_name,
                    campaign_id=click_data.content_object.campaign.campaign_key,
                    publisher=click_data.content_object.user.company_name,
                    publisher_id=click_data.content_object.user.pk,
                    ip_address=ip_address)
                if old_data:
                    return HttpResponse("Duplicate Key")
                else:
                    lead_data = ObjectLead.objects.create(
                        campaign=click_data.content_object.campaign.campaign_name,
                        campaign_id=click_data.content_object.campaign.campaign_key,
                        publisher=click_data.content_object.user.company_name,
                        publisher_id=click_data.content_object.user.pk,
                        ip_address=ip_address,
                        click_id=click_id_data)

        return HttpResponse("Done")
