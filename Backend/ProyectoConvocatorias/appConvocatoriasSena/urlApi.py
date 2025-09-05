from django.contrib import admin
from django.urls import path
from .viewsApis import * 
from rest_framework import include_docs_urls

urlpatterns = [
    path('convocatorias/', convocatoriaApi.as_view()),
    path('convocatorias/<int:pk>/', creatorDetailsApi.as_view()),
    path('docs/', include_docs_urls(title='Convocatorias API'))
    
]