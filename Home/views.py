from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import *
from django .contrib import messages

def land(request):
    template = loader.get_template('land.html')
    return HttpResponse(template.render())

def first(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def citrus(request):
    citrus_plants = CitrusPlant.objects.all()
    return render(request, 'citrus.html', {'citrus_plants': citrus_plants})

def berry(request):
    berry_plants = BerryPlant.objects.all()
    return render(request, 'berry.html', {'berry_plants': berry_plants})

def annuals(request):
    template = loader.get_template('annuals.html')
    return HttpResponse(template.render())

def perinnials(request):
    template = loader.get_template('perinnials.html')
    return HttpResponse(template.render())

def biennials(request):
    template = loader.get_template('biennials.html')
    return HttpResponse(template.render())

def airpurifier(request):
    airpurifier_plants = AirPurifierPlant.objects.all()
    return render(request, 'airpurifier.html', {'airpurifier_plants': airpurifier_plants})

def annuals(request):
    annual_plants = AnnualPlant.objects.all()
    return render(request, 'annuals.html', {'annual_plants': annual_plants})

def perinnials(request):
    perinnial_plants = PerinnialPlant.objects.all()
    return render(request, 'perinnials.html', {'perinnial_plants': perinnial_plants})

def biennials(request):
    biennial_plants = BiennialPlant.objects.all()
    return render(request, 'biennials.html', {'biennial_plants': biennial_plants})

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def search_plants_results(request):
    query = request.GET.get('q')
    
    citrus_results = CitrusPlant.objects.filter(name__icontains=query)
    berry_results = BerryPlant.objects.filter(name__icontains=query)
    annual_results = AnnualPlant.objects.filter(name__icontains=query)
    perinnial_results = PerinnialPlant.objects.filter(name__icontains=query)
    biennial_results = BiennialPlant.objects.filter(name__icontains=query)
    airpurifier_results = AirPurifierPlant.objects.filter(name__icontains=query)
    
    all_results = list(citrus_results) + list(berry_results) + list(annual_results) + list(perinnial_results) + list(biennial_results) + list(airpurifier_results)
    print("Query:", query)
    print("Citrus Results:", citrus_results.count())
    print("Berry Results:", berry_results.count())
    print("Annual Results:", annual_results.count())
    print("Perinnial Results:", perinnial_results.count())
    print("Biennial Results:", biennial_results.count())
    print("Air Purifier Results:", airpurifier_results.count())
    print("Total Results:", len(all_results))
    return render(request, 'search_results.html', {'results': all_results, 'query': query})

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('username')
        password = request.POST.get('password')
       
        
        account_details = User(
            username=name,
            email=email,
            password=password
        )
        
        account_details.save()
        return redirect('first')
    
    return render(request, 'sign_up.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            account = User.objects.get(username=username,password=password)
            print(account)
        except User.DoesNotExist:
            account = None
        if account is not None and account.password == password:
            return render(request, 'first.html')
        else:
            messages.error(request,'Invaid Login')
            return redirect('login')
    else:
        return render(request, 'login.html')

