from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Admission
from admissions.forms import AdmissionForm
# Create your views here.
def home(request):
    data =Admission.objects.all()
    admission_form = AdmissionForm()
    if request.method == "POST":
        result= AdmissionForm(request.POST)
        if result.is_valid():
           
            name = result.cleaned_data['name']
            email = result.cleaned_data['email']
            phone = result.cleaned_data['phone']
            date_of_birth = result.cleaned_data['date_of_birth']
            address = result.cleaned_data['address']

            results = Admission(
                name=name,
                email=email,
                phone=phone,
                date_of_birth=date_of_birth,
                address=address
            )
            results.save()
            # fs = open("admission.txt","a")
            # fs.write("\n........................................")
        
            # fs.write("\nname             :"+str(name))
            # fs.write("\nemail            :"+str(email))
            # fs.write("\nphone            :"+str(phone))
            # fs.write("\ndate_of_birth    :"+str(date_of_birth))
            # fs.close()

            return HttpResponse("Admission form submitted successfully!")

        else:
            return HttpResponse("Invalid form data. Please try again.")
    res = render(request,"home.html",{'data':data,'admission_form':admission_form})
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



