from django.urls import path

from . import views

urlpatterns = [
    path('track/', views.PostbackLead.as_view(), name='postbacktrack'),
]
