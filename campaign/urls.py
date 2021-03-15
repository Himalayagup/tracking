from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.CampaignCreate.as_view(), name='addcampaign'),
    path('', views.CampaignList.as_view(), name='campaignlist'),
    path('<pk>/update', views.CampaignUpdateView.as_view(),
         name='campaignupdate'),
    path('<pk>/detail', views.CampaignDetail.as_view(),
         name='campaigndetail'),
    path('<pk>/delete', views.CampaignDeleteView.as_view(),
         name='campaigndelete'),
    path('visit-slug/<pk>/', views.CampaignToPublisherDetail.as_view(),
         name='camppubdetail'),
]
