from django.contrib import admin
from django.urls import path, re_path
from profiles import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^profiles/(?P<profile_id>\d+)$', views.show)
]
