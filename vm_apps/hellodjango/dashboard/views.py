from django.shortcuts import render
from django.http import HttpResponse
import africastalking

# Create your views here.

def index(request):
   return render(request, "dashboard/index.html")

def profile(request):
   return render(request, "accounts/profile.html")

def sms(request):
   return render(request,"sms/send.html")

def airtime(request):
   return render(request,"airtime/index.html")

def voice(request):
   return render(request,"voice/index.html")

def payments(request):
   #return HttpResponse("Dashboard Payments home page.")
   return render(request,'payments/index.html')