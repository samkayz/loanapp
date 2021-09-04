from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='admin_sign'),
    path('home/', views.home, name='home'),
    path('signout/', views.signout, name='admin_signout'),
    path('emailconfig/', views.emailConfig, name='emailConfig'),
]