from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>Virat comptlete 1st 50th centuries in ODI</h1>')

def msd(request):
    return render(request,'msd.html')