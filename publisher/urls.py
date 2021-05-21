from django.urls import path

from . import views

urlpatterns = [
    # path('', views.HomePage.as_view(), name='home'),
    path('add/', views.publisher_register, name='addcamppub'),
    path('runningcamp/', views.CampaignToPublisherList.as_view(),
         name='runningcamplist'),
    path('<pk>/campaignlist/', views.PublisherDetail.as_view(),
         name='campaignlistpublisherwise'),
    path('', views.PublisherList.as_view(), name='publisherlist'),
    path('individual/', views.CampaignToPublisherIndividaulList.as_view(),
         name='publisherindividuallist'),
    path('<pk>/update/', views.CampaignToPublisherUpdateView.as_view(),
         name='camppubupdate'),
    path('<pk>/addpixel/', views.CampaignToPublisherPixelAddView.as_view(),
         name='camppubaddpixel'),
    path('<pk>/delete/', views.CampaignToPublisherDeleteView.as_view(),
         name='camppubdelete'),
    path('apply/<campaign_key>/', views.ApplyForCampaign.as_view(), name='join'),
    path('session/', views.ReadingSession.as_view(), name='reading_session'),
    path('manualassign/', views.CampaignToPublisherCreate.as_view(),
         name='mannualassign'),
    path('campaign/<pk>/data/', views.CampaignDataDetail.as_view(), name='datatata'),

]
