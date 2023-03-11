from django.shortcuts import render

# Create your views here.

def help_section(request):
    return render(request, 'help_section.html')