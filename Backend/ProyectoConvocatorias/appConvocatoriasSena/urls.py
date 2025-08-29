from django.contrib import admin
from django.urls import path
from . import viewsLider, views, viewsFuncionarios

urlpatterns = [
    # path("", views.home),
    path("addConvocatoria/", viewsLider.addConvocatoria, name="addConvocatoria"),
    path("addFuncionario/", viewsFuncionarios.addFuncionario, name="addFuncionario"),
]