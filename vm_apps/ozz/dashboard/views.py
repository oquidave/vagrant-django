from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import africastalking

# Create your views here.
@login_required
def index(request):
	#return HttpResponse("Dashboard home page.")
	return render(request, "includes/newbes.html")

@login_required
def sms(request):
	return render(request,'sms/send.html')

def airtime(request):
	return HttpResponse("Dashboard Airtime home page.")

def voice(request):
	return HttpResponse("Dashboard Voice home page.")

def payments(request):
	return HttpResponse("Dashboard Payments home page.")

@login_required
def profile(request):
   return render(request, "accounts/profile.html")

