from django.shortcuts import render

def app(request):
    return render(request, 'editor/list.html', {})