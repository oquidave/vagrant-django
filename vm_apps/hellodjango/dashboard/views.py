from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	#return HttpResponse("Dashboard home page.")
	return render(request, "dashboard/index.html")

def sms(request):
	return HttpResponse("Dashboard SMS home page.")

def airtime(request):
	return HttpResponse("Dashboard Airtime home page.")

def voice(request):
	return HttpResponse("Dashboard Voice home page.")

def payments(request):
	return HttpResponse("Dashboard Payments home page.")