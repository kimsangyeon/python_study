from django.shortcuts import render
from editor.models import Document
import json

def app(request):
    return render(request, 'editor/list.html', {})

def newDoc(request):
    return render(request, 'editor/index.html', {})

def getDocumentList(request):
    queryset = Document.objects.all()
    print(queryset)