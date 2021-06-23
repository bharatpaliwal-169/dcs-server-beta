from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control,never_cache
from .models import School,Contact
from .models import Partner,Insurance
from .models import Puc,Chauffer,Rto
from .forms import DriveForm
from .forms import PartnerForm
from .forms import ChaufferForm
from .forms import PucForm,InsuranceForm,RtoForm
import time

# Create your views here.
def home(request):
    if request.method == 'POST' and 'ContactForm' in request.POST:
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        phone = request.POST.get('phone')

        contact.name = name
        contact.email = email
        contact.comment = comment
        contact.phone = phone
        contact.save()

        return render(request,'ridit/success.html')
    '''if request.method == 'POST' and 'ChatBotForm' in request.POST:
        cb = ChatBot()
        msg = request.POST.get('msg')

        cb.msg = msg
        cb.save()'''
	
    return render(request,'ridit/home.html')
	
@login_required
@never_cache
def school(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DriveForm()
        else:
            employee = School.objects.get(pk=id)
            form = DriveForm(instance=employee)
        return render(request, "ridit/school.html", {'form': form})
    else:
        if id == 0:
            form = DriveForm(request.POST)
        else:
            employee = School.objects.get(pk=id)
            form = DriveForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/school.html", {'form': form})

def success(request):
    #if user is logged in then show the success page
    return render(request,"ridit/success.html")

def ch(request):
    return render(request,"ridit/ch.html")

@login_required
def partner(request):
    c = Partner()
    form=PartnerForm(request.POST or None, instance=c)
    if request.method=="POST":
        #print("success")
        if form.is_valid():
            f=form.save()
            f.save()
            return redirect('/success')
    return render(request, "ridit/partner.html", {'form':form})
'''def partner(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PartnerForm()
        else:
            employee = Partner.objects.get(pk=id)
            form = PartnerForm(instance=employee)
        return render(request, "ridit/partner.html", {'form': form})
    else:
        if id == 0:
            form = PartnerForm(request.POST)
        else:
            employee = Partner.objects.get(pk=id)
            form = PartnerForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/partner.html", {'form': form})
'''
@login_required
def chauffer(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ChaufferForm()
        else:
            employee = Chauffer.objects.get(pk=id)
            form = ChaufferForm(instance=employee)
        return render(request, "ridit/chauffer.html", {'form': form})
    else:
        if id == 0:
            form = ChaufferForm(request.POST)
        else:
            employee = Chauffer.objects.get(pk=id)
            form = ChaufferForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            day = request.POST['days']
            total = 499 * int(day)
            # messages.success(request, 'Your request is submitted successfully')
            return render(request,"ridit/ch.html",{'total':total})
        else:
            # messages.error(request,'error')
            return render(request, "ridit/chauffer.html", {'form': form})

@login_required
def puc(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PucForm()
        else:
            employee = Puc.objects.get(pk=id)
            form = PucForm(instance=employee)
        return render(request, "ridit/puc.html", {'form': form})
    else:
        if id == 0:
            form = PucForm(request.POST)
        else:
            employee = Puc.objects.get(pk=id)
            form = PucForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            vtype = request.POST['vehicle_type']
            total = 0
            if vtype=='2w':
                total=50
            elif vtype=='3w':
                total=150
            elif vtype=='4w':
                total=200
            elif vtype=='4cw':
                total=250
            else:
                total=500
            # messages.success(request, 'Your request is submitted successfully')
            return render(request,"ridit/p1.html",{'total':total})
        else:
            # messages.error(request,'error')
            return render(request, "ridit/puc.html", {'form': form})



def faq(request):
    return render(request,"faq/Main.html")

def driveFAQ(request):
    return render(request,"faq/driveFAQ.html")
def pucFAQ(request):
    return render(request,"faq/pucFAQ.html")

def chauffeurFAQ(request):
    return render(request,"faq/chauffeurFAQ.html")

def LicenseFAQ(request):
    return render(request,"faq/licenseFAQ.html")

def comming_soon(request):
    return render(request,"ridit/soon.html")

@login_required
@never_cache
def insurance(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = InsuranceForm()
        else:
            employee = Insurance.objects.get(pk=id)
            form = InsuranceForm(instance=employee)
        return render(request, "ridit/insurance.html", {'form': form})
    else:
        if id == 0:
            form = InsuranceForm(request.POST)
        else:
            employee = Insurance.objects.get(pk=id)
            form = InsuranceForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/insurance.html", {'form': form})

@login_required
@never_cache
def rto(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = RtoForm()
        else:
            employee = Rto.objects.get(pk=id)
            form = RtoForm(instance=employee)
        return render(request, "ridit/rto.html", {'form': form})
    else:
        if id == 0:
            form = RtoForm(request.POST)
        else:
            employee = Rto.objects.get(pk=id)
            form = RtoForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Your request is submitted successfully')
            return redirect('/success')
        else:
            # messages.error(request,'error')
            return render(request, "ridit/rto.html", {'form': form})
