from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, "payments/index.html")

def send(request):
	return HttpResponse("Payments send money.")