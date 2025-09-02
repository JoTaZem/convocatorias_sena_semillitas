from django.urls import path
from . import viewsLider, views

urlPatterns = [
    path("admin/", views.home),
    path("addConvocatoria/", viewsLider.addConvocatoria),
urlpatterns = [
    # path("", views.home),
    path("addConvocatoria/", viewsLider.addConvocatoria, name="addConvocatoria"),
]