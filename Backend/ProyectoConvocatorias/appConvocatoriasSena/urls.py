from django.contrib import admin
from django.urls import path
from . import viewsLider,views

urlPatterns = [
    path("", views.home),
    path("addConvocatoria", viewsLider.addConvocatoria),
]