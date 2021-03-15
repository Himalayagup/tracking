from django.contrib import admin
from campaign.models import Campaign, CampaignToPublisher
# Register your models here.
admin.site.register(Campaign)
admin.site.register(CampaignToPublisher)

# class PublisherCampaignInline(admin.TabularInline):
#     model = PublisherCampaign
