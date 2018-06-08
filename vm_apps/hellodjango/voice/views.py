from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, "voice/index.html")

def conf(request):
	return render(request, 'voice/conf.html')

def vhistory(request):
	return render(request, "voice/vhist.html")

def make_call(request):
	return HttpResponse("Make a voice call.")