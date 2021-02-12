from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('register/', views.register, name='register'),
    path('publisher_register/', views.publisher_register.as_view(),
         name='publisher_register'),
    path('manager_register/', views.manager_register.as_view(),
         name='manager_register'),
    path('owner_register/', views.owner_register.as_view(), name='owner_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
