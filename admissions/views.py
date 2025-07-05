from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Admission
# Create your views here.
def home(request):
    data =Admission.objects.all()
    res = render(request,"home.html",{'data':data})
    return res
def index(request):
    return render(request,"index.html",{})
def login(request):
    return render(request,"login.html",{})
def products(request):
    return render(request,"products.html",{})

def services(request):
    return render(request,"services.html",{})

def transport(request):
    return render(request,"transport.html",{})



