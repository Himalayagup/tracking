from django import forms
from campaign.models import CampaignToPublisher

# creating a form


class CampaignToPublisherForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = CampaignToPublisher

        # specify fields to be used
        fields = ["campaign",
                  ]


class CampaignToPublisherCreateForm(forms.ModelForm):
    class Meta:
        model = CampaignToPublisher
        fields = ["user", "campaign"]


class ApplyCampaignFormCreate(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = CampaignToPublisher

        # specify fields to be used
        fields = ["campaign",
                  ]
