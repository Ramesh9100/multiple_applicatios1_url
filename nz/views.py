from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def williamson(request):
    return HttpResponse('<h1>0 haters in cricket Kane Williamson</h1>')


def mitchell(request):
    return render(request,'mitchell.html')