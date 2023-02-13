from django.urls import path
from . import views

# app_name = "worklogger"
urlpatterns = [
    path('', views.home, name='home'),
]
