from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return render(request, 'home/base.html', {})

