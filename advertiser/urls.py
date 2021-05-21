from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.AdvertiserCreate.as_view(), name='addadvertiser'),
    path('', views.AdvertiserList.as_view(), name='advertiserlist'),
    path('<pk>/update', views.AdvertiserUpdateView.as_view(),
         name='advertiserupdate'),
    path('<pk>/delete', views.AdvertiserDeleteView.as_view(),
         name='advertiserdelete'),
]
