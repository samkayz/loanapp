from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='cus_logout'),
]
