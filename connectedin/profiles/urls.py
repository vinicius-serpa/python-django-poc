from django.contrib import admin
from django.urls import path, re_path
from profiles import views

urlpatterns = [
    re_path(r'^$', views.index)
]
