from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about.html')

def contact(request):
    return render(request, 'personal/contact.html')

def projects(request):
    return render(request, 'personal/projects.html')
