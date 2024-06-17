from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('home/', views.home_interface, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
]
