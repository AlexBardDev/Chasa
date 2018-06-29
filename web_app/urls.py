"""
This script contains the urls form my app.
"""
#Import libraries
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.events, name="events"),
    path("about/", views.about, name="about"),
]
