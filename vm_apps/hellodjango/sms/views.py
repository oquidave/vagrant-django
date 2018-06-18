from django.shortcuts import render,redirect
from django.http import HttpResponse
import africastalking
from .models import Smshist
from django.core import serializers


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
   if request.method == "POST":
      sms_stats = Smshist.objects.all()
      return render(request, "sms/smshist.html", {'sms_stats':sms_stats})

   elif request.method == "GET":
      sms_stats = Smshist.objects.all()
      return render(request,'sms/smshist.html',{'sms_stats':sms_stats})


def sacess(request):
   
      message = request.POST.get("sms_message")
      phone= request.POST.get("phone")


      api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
      username= "sandbox"
      africastalking.initialize(username=username,api_key=api_key)
      sms =africastalking.SMS
      response = sms.send(message,[phone])
      print(response)

      sms_stats = Smshist(content=message,status="sent", destination=phone)
      sms_stats.save()
      res=print(sms_stats)

      return redirect('smshistory')
   


def delete(request,id):
   print(id)
   d = Smshist.objects.get(id=id)
   d.delete()
   return redirect('smshistory')



