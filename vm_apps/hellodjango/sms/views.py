from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, "sms/index.html")

def send_sms(request):
	return HttpResponse("Send sms page.")