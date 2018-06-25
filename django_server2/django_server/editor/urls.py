from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app),
    path('newDoc/', views.newDoc),
    path('getDocumentList/', views.getDocumentList),
    # url(r'^getDocumentList/', views.getDocumentList, name='getDocumentList'),
    path('saveDocument/', views.saveDocument),
    path('updateDocument/', views.updateDocument),
    path('deleteDocument/', views.deleteDocument),
]
