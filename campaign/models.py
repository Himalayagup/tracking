from django.db import models
from django.urls import reverse
from advertiser.models import Advertiser
from accounts.models import Publisher
from analytics.models import ObjectViewed
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.
STATUS = (
    ("pending", "Pending"),
    ("active", "Active"),
    ("suspended", "Suspended"),
    ("declined", "Declined")
)

STATUS_CAMP = (
    ("pending", "Pending"),
    ("active", "Active"),
)

CAMPAIGN_TYPE_CHOICE = (
    ("cpl", "Cost Per Lead"),
    ("cpc", "Cost Per Click"),
    ("cpi", "Cost Per Impression"),
    ("cpa", "Cost Per Action"),
    ("cpv", "Cost Per Visit"),
    ("cps", "Cost Per Sale"),
    ("cpinstall", "Cost Per Install"),
    ("cpo", "Cost Per Open"),
    ("cpsm", "Cost Per Sent Mailer(s)"),
)
CAMPAIGN_CATEGORY_CHOICE = (
    ("banking", "Banking"),
    ("matrimony", "Matrimony"),
    ("job", "Job"),
    ("education", "Education"),
    ("finance", "Finance"),
    ("insurance", "Insurance"),
    ("securities", "Securities"),
    ("automobile", "Automobile"),
    ("travel_holidays", "Travel and Holidays"),
    ("realestate", "Real Estate"),
    ("ecommerce", "E Commerce"),
    ("classified", "Classified"),
    ("recharge_ecommerce", "Recharge & E Commerce"),
    ("recharge", "Recharge"),
    ("jewellery", "Jewellery"),
)


class Campaign(models.Model):
    advertiser = models.ForeignKey(
        Advertiser, related_name="advertiser_company",
        help_text="Advertiser Company Name",
        on_delete=models.CASCADE, null=True, blank=True,)
    campaign_name = models.CharField("Campaign Name",
                                     help_text="Enter the campaign name",
                                     max_length=235,)
    landing_url = models.URLField("Landing URL",
                                  help_text="Enter the landing url (must include http:// or https://)",
                                  max_length=300,)
    expire_url = models.URLField("Expire URL",
                                 help_text="Enter the expire url that will work when campaign ends (must include http:// or https://)",
                                 max_length=300,)
    start_date = models.DateField("Start Date",
                                  help_text="Enter the campaign's start date (format: YYYY-MM-DD)",
                                  )
    end_date = models.DateField("End Date",
                                help_text="Enter the campaign's end date (format: YYYY-MM-DD)",
                                )
    campaign_type = models.CharField("Campaign Type",
                                     help_text="Select the campaing types",
                                     max_length=22,
                                     choices=CAMPAIGN_TYPE_CHOICE,)
    campaign_category = models.CharField("Campaign Category",
                                         help_text="Select the campaing category",
                                         max_length=22,
                                         choices=CAMPAIGN_CATEGORY_CHOICE,
                                         null=True, blank=True)
    comment = models.TextField("Comments",
                               help_text="Any Comment(s)?",
                               null=True, blank=True)
    status = models.CharField("Status",
                              help_text="Choose the advertiser status",
                              max_length=22,
                              choices=STATUS,)
    publisher_campaign = models.ManyToManyField(
        Publisher, through="CampaignToPublisher", related_name='publisher_camp')
    campaign_key = models.AutoField(unique=True, primary_key=True,)

    def __str__(self):
        return self.campaign_name

    def get_absolute_url(self):
        return reverse('campaignlist')


class CampaignToPublisher(models.Model):
    user = models.ForeignKey(
        Publisher, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    pixel = models.URLField("Pigyback Pixel/URL", blank=True, null=True)
    status_cam = models.CharField("Status",
                                  help_text="Choose the publisher status",
                                  max_length=22,
                                  choices=STATUS_CAMP, default=STATUS_CAMP[0][0])
    val_obj = GenericRelation(ObjectViewed, object_id_field="object_id",
                              related_query_name="try_new")

    def __str__(self):
        return self.user.company_name

    class Meta:
        unique_together = ("user", "campaign")

    def get_absolute_url(self):
        return reverse('campaigntopublisherlist')
