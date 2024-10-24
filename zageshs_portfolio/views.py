from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

import os
def test():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)

from pathlib import Path
def test2():
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(os.path.join(BASE_DIR, 'staticfiles'))