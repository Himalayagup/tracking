import django_filters
from .models import Campaign


class CampaignStatusFilter(django_filters.FilterSet):

    class Meta:
        model = Campaign
        fields = ('status',)
