from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, "voice/index.html")

def make_call(request):
	return HttpResponse("Make a voice call.")