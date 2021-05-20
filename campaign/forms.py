from django import forms

from .models import Campaign

# creating a form


class CampaignForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Campaign

        # specify fields to be used
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


class PublisherCampaignForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = PublisherCampaign

        # specify fields to be used
        fields = ["campaign",
                  "publisher",
                  ]
