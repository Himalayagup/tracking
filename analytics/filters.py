import django_filters
from django_filters import DateRangeFilter, DateFilter
from campaign.models import CampaignToPublisher
from analytics.models import ObjectViewed, ObjectLead
from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class CampaignIndividaulFilter(django_filters.FilterSet):

    class Meta:
        model = CampaignToPublisher
        fields = ('campaign',)


class ClickViewFilter(django_filters.FilterSet):
    start_date = DateFilter(
        label='Start Date', field_name='timestamp', lookup_expr=('gt'),
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = DateFilter(
        label='End Date', field_name='timestamp', lookup_expr=('lt'), widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_range = DateRangeFilter(label='Date Range', field_name='timestamp',
                                 widget=forms.Select(
                                     attrs={'class': 'form-control'})
                                 )

    class Meta:
        model = ObjectViewed
        fields = ()


class LeadFilter(django_filters.FilterSet):
    start_date = DateFilter(
        label='Start Date', field_name='lead_timestamp', lookup_expr=('gt'),
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = DateFilter(
        label='End Date', field_name='lead_timestamp', lookup_expr=('lt'),
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_range = DateRangeFilter(
        label='Date Range', field_name='lead_timestamp',
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ObjectLead
        fields = ('campaign', 'publisher')

# Individual FilterSet


class ClickIndiFilter(django_filters.FilterSet):
    start_date = DateFilter(
        label='Start Date', field_name='timestamp', lookup_expr=('gt'))
    end_date = DateFilter(
        label='End Date', field_name='timestamp', lookup_expr=('lt'))
    date_range = DateRangeFilter(label='Date Range', field_name='timestamp',
                                 widget=forms.Select(
                                     attrs={'class': 'form-control'})
                                 )

    class Meta:
        model = ObjectViewed
        fields = ()


class LeadIndiFilter(django_filters.FilterSet):
    start_date = DateFilter(
        label='Start Date', field_name='lead_timestamp', lookup_expr=('gt')
    )
    end_date = DateFilter(
        label='End Date', field_name='lead_timestamp', lookup_expr=('lt'))
    date_range = DateRangeFilter(
        label='Date Range', field_name='lead_timestamp',
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ObjectLead
        fields = ()
