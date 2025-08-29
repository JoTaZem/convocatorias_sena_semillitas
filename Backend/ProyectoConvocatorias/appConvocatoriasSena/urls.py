from django.urls import path
from . import viewsLider, views

urlpatterns = [
    # path("", views.home),
    path("addConvocatoria/", viewsLider.addConvocatoria, name="addConvocatoria"),
]