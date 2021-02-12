from django.urls import path

from . import views

urlpatterns = [
    path('', views.ObjectViewedList.as_view(), name='visitlist'),
    path('leads/', views.ObjectLeadList.as_view(), name='leadlist'),
    path('campaign-wise-report/', views.CampaignWiseReport.as_view(),
         name='campaignwisereport'),
    path('campaign/<pk>/detail/', views.RunningCampaignsReportDetail.as_view(),
         name='camapignwisedetailedreport'),
    path('reports/', views.CampaignIndividaulList.as_view(),
         name='campaign_reports'),
    path('reports/<pk>/detail/', views.CampaignDataIndiDetail.as_view(),
         name='campaign_reports_indi')
]
