from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import africastalking
import re
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
def sms_tiles(request):
   return render(request, "sms/sms_tiles.html")

@login_required
def send_sms(request):
   if request.method =="POST":
      #get    
      message = request.POST.get("sms_message")
      name = request.POST.get("name")
      phone= request.POST.get("phone")
      #initiate gateway
      api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
      username= "sandbox"
      africastalking.initialize(username=username,api_key=api_key)
      sms =africastalking.SMS
      #send
      response = sms.send(message,[phone])
      #save history
      sms_stats = Smshist(name=name,content=message,status="sent", destination=phone)
      sms_stats.save()
      return redirect('smshistory')
   else:
      return render(request,'sms/send.html')

#csv download
@login_required
def sms_csv_download(request): 
   import csv

   """ Renders a csv list  """
   response = HttpResponse(content_type='csv')
   response['Content-Disposition'] = 'attachment; filename=sample.csv'
   writer = csv.writer(response, dialect=csv.excel)
   writer.writerow(['Name','Contact'])
   writer.writerow(['name_1','name1_contact'])
   writer.writerow(['name_2','name2_contact'])
   return response



@login_required
def bulks(request):
   data = {}
   if request.method == "POST":
      #get 
      message=request.POST.get('sms_message')
      csv_file = request.FILES["browse"]
      #read into file
      file_data = csv_file.read().decode("utf-8")
      #split at line end
      rowz = re.split('\n', file_data)
      #what I want      
      recipients = []      
      for user in rowz[1:]:
         user_items = re.split(',',user)
         if len(user_items)>1:
            recipient = {}
            recipient['name']= user_items[0]
            recipient['phoneNumber'] = "+256"+user_items[1]
            recipients.append(recipient)
            #save history
            sms_stats = Smshist(name=user_items[0],content=message,status="sent", destination="+256"+user_items[1])
            sms_stats.save() 
            #send
            api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
            username = 'sandbox'
            africastalking.initialize(username=username,api_key=api_key)
            sms =africastalking.SMS
            response = sms.send(message,["+256"+user_items[1]])           
         else:
            pass     
      #history
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
def sms_schedule(request):
   return render(request,"sms/sms_schedule.html")
   
#deletes
#sms hist item delete
@login_required
def delete(request,id):
   print(id)
   id_match = Smshist.objects.get(id=id)
   id_match.delete()
   messages.add_message(request, messages.INFO, 'Item Deleted')
   return redirect('smshistory')

#sms hist table delete
@login_required
def smshist_delete(request):
   if request.method == "GET":
      hist_delete = Smshist.objects.all()
      hist_delete.delete()
      return redirect('smshistory')
   else:
      return redirect('smshistory')



