from django.shortcuts import render, redirect
import requests
import json
from .models import *
import folium
from folium import plugins
from .forms import PropertyRegister, RegistrationForm, ContactForm
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def home_page(request):
	if request.method == 'POST':
		info = Contact.objects.create(name=request.POST.get('name'), email=request.POST.get('email'), subject=request.POST.get('subject'), message=request.POST.get('message'))
		info.save()
		return redirect('/')
	else:
		formContact = ContactForm()
	return render(request, 'index.html', {'formContact':formContact})

@login_required
def map_page(request):
	data_list = Location.objects.values_list('latitude', 'longitude')
	map1 = folium.Map(location=[-1.952183, 30.054957], tiles='OpenStreetMap', zoom_start=9.5)
	plugins.FastMarkerCluster(data_list, icon=None).add_to(map1)

	map1 = map1._repr_html_()

	context = {
		'map1' : map1,
	}
	return render(request, 'map.html', context)

@login_required
def get_detail(request):
	if request.method == 'POST':
		ip = requests.get('https://api.ipify.org?format=json')
		ip_data = json.loads(ip.text)
		res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
		location_data_one = res.text
		location_data = json.loads(location_data_one)

		info = Location(title =request.POST.get('title'), poster=request.user,country=location_data['country'], latitude=location_data['lat'], longitude=location_data['lon'],
		city=request.POST.get('inputCity'), image=request.FILES.get('photo'), description=request.POST.get('message'),
		district=request.POST.get('inputDistrict'), sector=request.POST.get('inputSector'))
		info.save()
		messages.success(request, f'Report is successfull!')
		return redirect('home')
	else:
	
		form=PropertyRegister()
	
	return render(request, 'report_form.html', context = {'form':form})

@login_required
def dashboard(request):
	contacts = Contact.objects.all()
	datas = Location.objects.all()
	number_problem = datas.count()
	contacts=Contact.objects.all()
	users = User.objects.all()
	number_user = users.count()
	incompletes = Location.objects.filter(status=False)
	number_incomplete = incompletes.count()
	completes = Location.objects.filter(status=True)
	number_complete =completes.count()
	messages = Contact.objects.all()
	
	data_list = Location.objects.values_list('latitude', 'longitude')
	map1 = folium.Map(location=[-1.952183, 30.054957], tiles='OpenStreetMap', zoom_start=9.5)
	plugins.FastMarkerCluster(data_list, icon=None).add_to(map1)

	map1 = map1._repr_html_()

	context = {
		'map1' : map1,
		'datas':datas,
		'contacts':contacts,
		'users':users,
		'incompletes':incompletes,
		'completes':completes,
		'number_user':number_user,
		'number_incomplete':number_incomplete,
		'number_complete':number_complete,
		'number_problem':number_problem,
		'messages':messages,
	}
	return render(request, 'dashboard.html', context)


def registration(request):
    context = {}
    context['form'] = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('get_detail')
        else:
            context['form'] = form
    return render(request,'signup.html',context)


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print(user.is_staff)
				if user.is_staff == True:
					return redirect("dashboard")
				else:
					return redirect("home")

			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

@login_required
def detail(request, id):
	single_list = Location.objects.filter(pk=id).values_list('latitude', 'longitude')
	map1 = folium.Map(location=[-1.952183, 30.054957], tiles='OpenStreetMap', zoom_start=9.5)
	plugins.FastMarkerCluster(single_list, icon=None).add_to(map1)

	map1 = map1._repr_html_()

	obj = get_object_or_404(Location,pk=id)

	context = {
		'map1' : map1,
		'obj':obj,
	}
	return render(request, 'detail.html', context)


@login_required
def profile(request):
	return render(request, 'profile.html')


def contact(request):
	if request.method=="POST":
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		message=request.POST.get('message')

		en=Contact(name=name,email=email,subject=subject,message=message)
		en.save()
		
	return redirect('contact')
	
	return render(request, 'index.html', {'formContact': formContact})

def completeProblem(request, id):
	problem = Location.objects.get(pk=id)
	problem.status = True
	problem.save()

	return redirect('dashboard')