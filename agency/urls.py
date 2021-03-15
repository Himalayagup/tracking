from django.urls import path

from . import views

urlpatterns = [
    # path('', views.HomePage.as_view(), name='home'),
    path('add/', views.AgencyCreate.as_view(), name='addagency'),
    path('', views.AgencyList.as_view(), name='agencylist'),
    path('<pk>/update', views.AgencyUpdateView.as_view(), name='agencyupdate'),
    path('<pk>/delete', views.AgencyDeleteView.as_view(), name='agencydelete'),
]
