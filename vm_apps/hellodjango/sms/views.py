from django.shortcuts import render,redirect
from django.http import HttpResponse
import africastalking
from .models import Smshist
from django.core import serializers
import csv
import codecs


# Create your views here.

def index(request):
   return render(request, "sms/index.html")

def send_sms(request):
   if request.method =="POST":
      return render(request,"sms/sms.html",{"sms_message":message,"phone":phone})
   else:
      return render(request,'sms/send.html')


def bulks(request):
   data = {}
   if request.method == "POST":
      #get message content
      message=request.POST.get('sms_message')

      #get file content
      csv_file = request.FILES["browse"]

      #read into file
      file_data = csv_file.read().decode("utf-8")
      #split into lines
      lines = file_data.split(',')
      print(lines)

      #make set
      s = set(lines)
      print(s)

      #iterate over set and lines
      for no in s:
         for no in lines:
            print(no)
            #instatiate Africa's talking api
            api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
            username= "sandbox"
            africastalking.initialize(username=username,api_key=api_key)
            sms =africastalking.SMS
         
            #send
            response = sms.send(message,[no])
            print(response)
            #save to model
            sms_stats = Smshist(content=message,status="sent", destination=no)
            sms_stats.save()
            #res=print(sms_stats)
            #redirect to history
            
         return redirect('smshistory')
   elif request.method=="GET":
      return render(request, 'sms/bulks.html',data)
   else:
      return render(request,'sms/bulks.html')
 


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



