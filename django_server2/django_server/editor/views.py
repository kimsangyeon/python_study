from django.shortcuts import render
from editor.models import Document
from django.http import HttpResponse
import json

def app(request):
    return render(request, 'editor/list.html', {})

def newDoc(request):
    return render(request, 'editor/index.html', {})

def getDocumentList(request):
    queryset = Document.objects.all()
    return HttpResponse(json.dumps({"document": list(queryset)}))

def saveDocument(request):
    if request.method == 'POST':
        request_data = ((request.body).decode('utf-8'))
        request_data = json.loads(request_data)

        doc = Document(editor=request_data['editor'], title=request_data['title'], html=request_data['html'], css=request_data['css'])
        doc.save()

def updateDocument(request):
    if request.method == 'POST':
        request_data = ((request.body).decode('utf-8'))
        request_data = json.loads(request_data)
        id = request_data['id']

        doc = Document.objects.get(pk=id)
        doc.editor = request_data['editor']
        doc.title = request_data['title']
        doc.html = request_data['html']
        doc.css = request_data['css']
        doc.save()

def deleteDocument(request):
    if request.method == 'POST':
        request_data = ((request.body).decode('utf-8'))
        request_data = json.loads(request_data)
        id = request_data['id']

        doc = Document.objects.get(pk=id)
        doc.delete()