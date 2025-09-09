from django.contrib import admin
from django.urls import path
from .viewsApi import TipoConvocatoriaList, TipoConvocatoriaDetail, ConvocatoriaList, ConvocatoriaDetail, AprendizList, AprendizDetail
from appConvocatoriasSena import viewsApi

from rest_framework.documentation import include_docs_urls

urlpatterns=[
    path('listarConvocatorias/', ConvocatoriaList.as_view()),
    path("tipoConvocatoria/", TipoConvocatoriaList.as_view()),
    path("tipoConvocatoria/<int:pk>/", TipoConvocatoriaDetail.as_view()),
    path("convocatoria/", ConvocatoriaList.as_view()),
    path("convocatoria/<int:pk>/", ConvocatoriaDetail.as_view()),
    path("aprendiz/", AprendizList.as_view()),
    path("aprendiz/<int:pk>/", AprendizDetail.as_view()),
    path ("docs/",include_docs_urls(title="Documentacion Api")),
]
