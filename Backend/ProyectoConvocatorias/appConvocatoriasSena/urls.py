from django.contrib import admin
from django.urls import path
from . import viewsLider,views

urlPatterns = [
    path("admin/", views.home),
    path("addConvocatoria/", viewsLider.addConvocatoria),
]