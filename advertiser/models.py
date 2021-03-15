from django.db import models
from django.urls import reverse
from agency.models import Agency
# Create your models here.

CATEGORY_CHOICE = (
    ("Affiliate", "Affiliate"),
    ("Affiliate_Network", "Affiliate Network"),
    ("Branding", "Branding"),
    ("Direct", "Direct"),
    ("Lead_Generation", "Lead Generation"),
    ("Arbitrage", "Arbitrage")
)
STATUS = (
    ("pending", "Pending"),
    ("active", "Active"),
    ("suspended", "Suspended"),
    ("declined", "Declined")
)


class Advertiser(models.Model):
    agency = models.ForeignKey(
        Agency, related_name="advertiser_agency", on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField("Company Name",
                                    help_text="Enter the company/brand name",
                                    max_length=150,)
    first_name = models.CharField("First Name",
                                  max_length=150,)
    last_name = models.CharField("Last Name",
                                 max_length=150,)
    email = models.EmailField("Mail ID",
                              help_text="Enter mail id",
                              max_length=300,)
    advertiser_category = models.CharField("Advertiser Category",
                                           help_text="Which category best describes the primary offers you will be advertising?",
                                           max_length=22,
                                           choices=CATEGORY_CHOICE,)
    status = models.CharField("Status",
                              help_text="Choose the advertiser status",
                              max_length=22,
                              choices=STATUS,)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('advertiserlist')
