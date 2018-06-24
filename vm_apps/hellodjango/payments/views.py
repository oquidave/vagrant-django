from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
	return render(request, "payments/index.html")

@login_required
def phistory(request):
	return render(request, 'payments/phist.html')

@login_required
def send(request):
	return HttpResponse("Payments send money.")