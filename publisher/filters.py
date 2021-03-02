import django_filters
from django_filters import DateRangeFilter, DateFilter
from campaign.models import CampaignToPublisher


class CampaignStatuFilter(django_filters.FilterSet):

    class Meta:
        model = CampaignToPublisher
        fields = ('status_cam',)
