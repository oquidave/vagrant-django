from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import Athist
from .models import Buyhist
from .models import Bulkhist
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import africastalking

# Create your views here.
@login_required
def index(request):
	return render(request, "airtime/mm_buy.html")

@login_required
def csv_download(request): 
	import csv

	""" Renders a csv list  """
	response = HttpResponse(content_type='csv')
	response['Content-Disposition'] = 'attachment; filename=sample.csv'
	writer = csv.writer(response, dialect=csv.excel)
	writer.writerow(['Name', 'Contact','Amount'])
	print(response)
	return response


@login_required
def atbulk(request):
	data={}
	if "POST" == request.method:
		
		amount=request.POST.get('amount')
		
		#get file content
		csv_file = request.FILES["contacts"]
		
		#read into file
		file_data = csv_file.read().decode("utf-8")
		
		#split into lines
		lines = file_data.split(',')

		#filter thru
		new_list = [lines[i:i+3] for i in range(0, len(lines), 3)]
		valid_lines = [num for num in new_list[:3] if num != '\n']
		
		#make set
		set_lines = set(lines)
		print(valid_lines)
		#filter set
		valid_numbers = [num for num in set_lines if len(num)>3]
		
		#iterate over nums
		for no in valid_lines:
			for no in valid_numbers:

							
				#instatiate Africa's talking api
				api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
				username= "sandbox"
				africastalking.initialize(username=username,api_key=api_key)
				airtime =africastalking.Airtime

				#send
				res = airtime.send(phone_number=no,amount="UGX "+amount)
				
				#save to model
				users = Bulkhist(amount=amount,status="sent", destination=no)
				users.save()				
				
				#redirect to history 
			return redirect('bulkhist')
	elif request.method=="GET":
		stats = Bulkhist.objects.all()
		return render(request, 'airtime/atbulk.html',{"stats":stats})


@login_required
def history(request):
	return render(request,"airtime/history.html")


@login_required
def at_subscribe(request):
	return render(request,"airtime/at_subscribe.html")


@login_required
def bulkhist(request):
	if request.method == "POST":
		stats = Bulkhist.objects.order_by("-date")
		return render( request,"airtime/bulkhist.html",{"stats":stats})
	elif request.method == "GET":
		stats = Bulkhist.objects.order_by("-date")
		page = request.GET.get('page', 1)
		paginator = Paginator(stats, 15)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
		
		return render( request,"airtime/bulkhist.html",{"users":users})



@login_required
def mm_history(request):
	#mobile money buy history
	if request.method == "POST":
		stats = Athist.objects.all()
		return render( request,"airtime/mm_history.html",{"stats":stats})
	elif request.method == "GET":
		stats = Athist.objects.order_by("-date")
		page = request.GET.get('page', 1)
		paginator = Paginator(stats, 15)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
		
		return render( request,"airtime/mm_history.html",{"users":users})


@login_required  
def ozz_history(request):
	#at account buy history
	if request.method == "POST":
		stats = Buyhist.objects.all()
		return render( request,"airtime/ozz_history.html",{"stats":stats})
	elif request.method == "GET":
		stats = Buyhist.objects.order_by("-date")
		page = request.GET.get('page', 1)
		paginator = Paginator(stats, 15)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)		
		return render( request,"airtime/ozz_history.html",{"users":users})
  
	


def pay(phone, amount):
	
	api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
	username = 'sandbox'

	africastalking.initialize(username=username,api_key=api_key)
	airtime = africastalking.Airtime
	res = airtime.send(phone_number=phone,amount="UGX "+amount)
	print(res)
	if res.get('status') == 'sent':
		return redirect('history')
	else:
		return redirect('buy1')
	

@login_required
def at(request):
	if request.method == 'POST':

	   # try:
	    chargephone = request.POST.get('chargephone')
	    amount = request.POST.get('amount')
	    phone = request.POST.get('phone')

	    api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
	    username = 'sandbox'

	    africastalking.initialize(username=username,api_key=api_key)		
	    productName  = "0zz"
	    # The phone number of the customer checking out
	    phoneNumber=chargephone
	    
	    # The 3-Letter ISO currency code for the checkout amount
	    currencyCode = "UGX"
	   	
	   
	    metadata = {"agentId" : "654","productId" : "321"}
	    
	    
	    payment = africastalking.Payment
	    
	    res = payment.mobile_checkout(product_name=productName, phone_number=chargephone, currency_code=currencyCode, amount=amount, metadata=metadata)
	    
	    if(res.get('status') == 'PendingConfirmation'):
	    	pay(phone, amount)
	    	stats = Athist(amount=amount,status="sent", destination=phone,source=chargephone)
	    	stats.save()
	    	res=print(stats)
	    	return redirect('mm_history')
	    else:
	    	print('No money')
	    return redirect('mm_history')

@login_required
def buy(request):
	if request.method == "POST":
		amount = request.POST.get('amount')
		phone = request.POST.get('phone')
		pay(phone, amount)
		stats = Buyhist(amount=amount,status="sent", destination=phone)
		stats.save()
		return redirect('ozz_history')
	else:
		return render(request,'airtime/buy.html')


@login_required
def at_buy(request):
	return render(request,'airtime/at_buy.html')


@login_required
def rm(request,id):
	if request.method == "GET":
		object_match = Bulkhist.objects.get(id=id)
		object_match.delete()
		messages.add_message(request, messages.INFO, 'Item Deleted')
		return redirect('bulkhist')
	else:
		return redirect('bulkhist')



@login_required
def delit(request,id):
	if request.method == "GET":
		id_match = Athist.objects.get(id=id)
		id_match.delete()
		messages.add_message(request, messages.INFO, 'Item Deleted')
		return redirect('mm_history')
	else:
		return redirect('mm_history')



@login_required
def drop_table(request):
	if request.method == "GET":
		drop_Bulkhist = Bulkhist.objects.all()
		drop_Bulkhist.delete()
		return redirect('bulkhist')
	else:
		return redirect('bulkhist')




@login_required
def delete(request,id):
	if request.method == "GET":
		print(id)
		id_match = Buyhist.objects.get(id=id)
		id_match.delete()
		messages.add_message(request, messages.INFO, 'Item Deleted')
		return redirect('ozz_history')
	else:
		return redirect('ozz_history')



	



	    