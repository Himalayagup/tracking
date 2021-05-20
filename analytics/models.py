import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .signals import object_lead_signal, object_viewed_signal
from .utils import (get_campaign, get_campaign1, get_campaign_id,
                    get_campaign_id1, get_client_ip, get_publisher,
                    get_publisher1, get_publisher_id, get_publisher_id1)

# Create your models here.


class UniqueID(models.Model):
    uniqueid = models.UUIDField(
        null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.uniqueid)

# click/visit recorder
# Click/Visit Model


class ObjectViewed(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField()
    ip_address = models.CharField(max_length=120, blank=True, null=True)
    content_object = GenericForeignKey(
        'content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    click_id = models.UUIDField(
        null=True, blank=True, unique=True)

    def __str__(self, ):
        return "%s viewed: %s & IP Address %s" % (self.content_object, self.timestamp, self.ip_address)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'


# Click/Visit Model Data Receiver


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    ip_address = None
    try:
        # get_client_ip is utility in utils.py file to store IP address
        ip_address = get_client_ip(request)
    except:
        pass
    # getting unique id generated from utils.py file
    from campaign.utils import get_uni_id
    try:
        global unique_click_id
        unique_click_id = get_uni_id()
    except:
        pass

    new_view_instance = ObjectViewed.objects.create(
        content_type=c_type,
        object_id=instance.id,
        ip_address=ip_address,
        click_id=unique_click_id
    )


# Click/Visit Model Data Receiver connection with click/visit signal
object_viewed_signal.connect(object_viewed_receiver)

# Leads checking

# Leads Storing Model


class ObjectLead(models.Model):
    campaign = models.CharField(max_length=235)
    campaign_id = models.PositiveIntegerField()
    publisher = models.CharField(max_length=100)
    publisher_id = models.PositiveIntegerField()
    lead_timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(
        max_length=120, blank=True, null=True)
    click_id = models.UUIDField(
        null=True, blank=True, unique=True)

    def __str__(self, ):
        return "%s lead: %s & IP Address %s" % (self.campaign, self.lead_timestamp, self.ip_address)

    class Meta:
        ordering = ['-lead_timestamp']
        verbose_name = 'Object Lead'
        verbose_name_plural = 'Objects Lead'

# Leads Model Data Receiver


def object_lead_receiver(sender, instance, request, *args, **kwargs):
    campaign = None
    campaign_id = None
    publisher = None
    publisher_id = None
    ip_address = None
    # to get ip
    try:
        # get_client_ip is utility in utils.py file to get IP address
        ip_address = get_client_ip(request)
    except:
        pass

    # to get publisher name
    try:
        # get_publisher is utility in utils.py file to get publisher name
        publisher_n = get_publisher(request)
    except:
        pass

    # to get publisher id
    try:
        # get_publisher_id is utility in utils.py file to get publisher id
        publisher_n_id = get_publisher_id(request)
    except:
        pass

    # to get campaign name
    try:
        # get_campaign is utility in utils.py file to get campaign name
        campaign_n = get_campaign(request)
    except:
        pass

    # to get campaign id
    try:
        # get_campaign_id is utility in utils.py file to get campaign id
        campaign_n_id = get_campaign_id(request)
    except:
        pass

    #COOKIES###################################################################
    # to get publisher name
    try:
        # get_publisher is utility in utils.py file to get publisher name
        publisher_n1 = get_publisher1(request)
    except:
        pass

    # to get publisher id
    try:
        # get_publisher_id is utility in utils.py file to get publisher id
        publisher_n_id1 = get_publisher_id1(request)
    except:
        pass

    # to get campaign name
    try:
        # get_campaign is utility in utils.py file to get campaign name
        campaign_n1 = get_campaign1(request)
    except:
        pass

    # to get campaign id
    try:
        # get_campaign_id is utility in utils.py file to get campaign id
        campaign_n_id1 = get_campaign_id1(request)
    except:
        pass

    # if request.COOKIES:
    #     new_lead_instance = ObjectLead.objects.get_or_create(
    #         campaign=request.COOKIES['campaign1'],
    #         campaign_id=request.COOKIES['campaign_id1'],
    #         publisher=request.COOKIES['publisher1'],
    #         publisher_id=request.COOKIES['publisher_id1'],
    #         ip_address=ip_address,
    #     )
    # else:
    #     pass
    # if request.session.keys():
    #     new_lead_instance = ObjectLead.objects.get_or_create(
    #         campaign=campaign_n,
    #         campaign_id=campaign_n_id,
    #         publisher=publisher_n,
    #         publisher_id=publisher_n_id,
    #         ip_address=ip_address,
    #     )
    # else:
    #     pass
    if request.COOKIES:
        new_lead_instance = ObjectLead.objects.get_or_create(
            campaign=campaign_n1,
            campaign_id=campaign_n_id1,
            publisher=publisher_n1,
            publisher_id=publisher_n_id1,
            ip_address=ip_address,
        )
    else:
        pass


object_lead_signal.connect(object_lead_receiver)
