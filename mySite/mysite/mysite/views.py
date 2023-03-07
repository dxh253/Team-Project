from django.shortcuts import render


def helpSection(request):
    return render(request, 'helpSection.html')

def homepage(request):
    return render(request, 'homepage.html')
