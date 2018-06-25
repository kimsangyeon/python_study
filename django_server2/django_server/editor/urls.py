from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app),
    path('newDoc/', views.newDoc),
    path('getDocumentList/', views.getDocumentList),
]
