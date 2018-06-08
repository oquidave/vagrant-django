from django.shortcuts import render
from django.http import HttpResponse
from ATLib import AfricasTalkingGateway
from ATLib.AfricasTalkingGateway import AfricasTalkingGatewayException
import africastalking


# Create your views here.
def index(request):
   return render(request, "sms/index.html")

def send_sms(request):
   if request.method =="POST":
      return render(request,"sms/sms.html",{"sms_message":message,"phone":phone})
   else:
      return render(request,'sms/send.html')


def bulks(request):
   return render(request, 'sms/bulks.html')


def smshistory(request):
   return render(request, "sms/smshist.html")


def sacess(request):
   if request.method =="POST":
      message = request.POST.get("sms_message")
      phone= request.POST.get("phone")
      api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
      username= "sandbox"
      africastalking.initialize(username=username,api_key=api_key)
      sms =africastalking.SMS
      response = sms.send(message,[phone])
      print(response)
      return render(request,'sms/smserr.html')
   else:
      return render(request, 'sms/send')
