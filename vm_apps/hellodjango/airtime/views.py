from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, "airtime/index.html")

def send_airtime(request):
	return HttpResponse("Send Airtime ")