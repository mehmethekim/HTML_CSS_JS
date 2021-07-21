from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def mehmet(request):
     return HttpResponse("HELLO MEHMET")
def input(request,name):
    return HttpResponse(f"Hello , {name}")

