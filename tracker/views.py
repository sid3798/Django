from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker import views as tracker_views
from .forms import PatientAdmitForm
from .models import Patient
from django.http import HttpResponse

# Create your views here.
def home(request):
    context={}
    return render(request,'home.html')

@login_required(login_url='/accounts/login') 
def patients(request):
    form = PatientAdmitForm()
    list_of_patients = Patient.objects.all()[:10]
    #context = {'list_of_patients':list_of_patients}
    context = {'list_of_patients':list_of_patients,'admin':'Neemit'}
    return render(request,'patient.html',context) 

def add_patient(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    diagnoses = request.POST.get('diagnoses')

    p_add = Patient(name=name,age=age,diagnoses=diagnoses)
    p_add.save()
    return HttpResponse("success")       

def reports(request):
    context={}
    return render(request,'reports.html')

           