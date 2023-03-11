from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def vue_homepage(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')
