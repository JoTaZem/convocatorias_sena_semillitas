from django.contrib import admin
from django.urls import path
from .viewsApi import *
from rest_framework.documentation import include_docs_urls

urlpatterns=[
    path("convocatoria/", ConvocatoriaList.as_view()),
    path("convocatoria/<int:pk>/", ConvocatoriaDetail.as_view()),
    path ("docs/",include_docs_urls(title="Documentacion Api")),
]
from django.contrib import admin
from django.urls import path
from viewsApi import *
from rest_framework.documentation import include_docs_urls

urlpatterns=[
    path("convocatoria/", ConvocatoriaList.as_view()),
    path("convocatoria/<int:pk>/", ConvocatoriaDetail.as_view()),
    path ("docs/",include_docs_urls(title="Documentacion Api")),
]
