from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import africastalking
from django.contrib import messages
from .models import Smshist
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import csv
import codecs


# Create your views here.

@login_required
def index(request):
   return render(request, "sms/index.html")

@login_required
def send_sms(request):
   if request.method =="POST":
      return render(request,"sms/sms.html",{"sms_message":message,"phone":phone})
   else:
      return render(request,'sms/send.html')

@login_required
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
      #filterthrough
      sot = [num for num in lines if num != '\n']
      print(sot)

      #make set
      s = set(lines)
      print(s)
      #filterthrough
      x = [num for num in s if len(num)>3]
      print(x)

      #iterate over set and lines
      for no in sot:
         for no in x:
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
 

@login_required
def smshistory(request):
   if request.method == "POST":
      sms_stats = Smshist.objects.order_by("-date")
      return render(request, "sms/smshist.html", {'sms_stats':sms_stats})

   elif request.method == "GET":
      sms_stats = Smshist.objects.order_by("-date")
      page = request.GET.get('page', 1)
      paginator = Paginator(sms_stats, 15)
      try:
         users = paginator.page(page)
      except PageNotAnInteger:
         users = paginator.page(1)
      except EmptyPage:
         users = paginator.page(paginator.num_pages)
      
      return render(request,'sms/smshist.html',{'users':users})

@login_required
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



@login_required
def sms_schedule(request):
   return render(request,"sms/sms_schedule.html")
   

@login_required
def delete(request,id):
   print(id)
   id_match = Smshist.objects.get(id=id)
   id_match.delete()
   messages.add_message(request, messages.INFO, 'Item Deleted')
   return redirect('smshistory')



