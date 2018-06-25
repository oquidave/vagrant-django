from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Athist
from .models import Buyhist
from .models import Bulkhist
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import africastalking

# Create your views here.
@login_required
def index(request):
	return render(request, "airtime/index.html")

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
		print(lines)
		#filter thru
		sot = [num for num in lines if num != '\n']
		print(sot)
		#make set
		s = set(lines)
		print(s)
		#filter set
		t = [num for num in s if len(num)>3]
		print(t)

		#iterate over nums
		for no in sot:
			for no in t:
				print(no)
				
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
				
				#res=print(sms_stats)
				print(res)
				#redirect to history 
			return redirect('bulkhist')

	elif request.method=="GET":
		stats = Bulkhist.objects.all()
		return render(request, 'airtime/atbulk.html',{"stats":stats})


@login_required
def history(request):
	return render(request,"airtime/history.html")

@login_required
def bulkhist(request):
	if request.method == "POST":
		stats = Bulkhist.objects.all()
		return render( request,"airtime/bulkhist.html",{"stats":stats})
	elif request.method == "GET":
		stats = Bulkhist.objects.all()
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
def athistory(request):
	if request.method == "POST":
		stats = Athist.objects.all()
		return render( request,"airtime/athist.html",{"stats":stats})
	elif request.method == "GET":
		stats = Athist.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(stats, 15)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
		
		return render( request,"airtime/athist.html",{"users":users})


@login_required  
def buyhistory(request):
	if request.method == "POST":
		stats = Buyhist.objects.all()
		return render( request,"airtime/buyhist.html",{"stats":stats})
	elif request.method == "GET":
		stats = Buyhist.objects.all()
		stats = Athist.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(stats, 15)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
		
		return render( request,"airtime/buyhist.html",{"users":users})
  
	

@login_required
def pay(phone, amount):
	#return render(request,'airtime/pay.html')
	#if request.method == 'POST':
		#phone = request.POST.get('phone')
		#amount = request.POST.get('amount')

	api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
	username = 'sandbox'

	africastalking.initialize(username=username,api_key=api_key)
	airtime = africastalking.Airtime
	res = airtime.send(phone_number=phone,amount="UGX "+amount)
	print(res)
	if res.get('status') == 'sent':
		return redirect('xs')
	else:
		return redirect('era')
	

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
	    # The checkout amount
		
	    # Any metadata that you would like to send along with this request
	    # This metadata will be  included when we send back the final payment notification
	    metadata = {"agentId" : "654","productId" : "321"}
	    #africastalking.initialize(username=username,api_key=api_key)
	    
	    payment = africastalking.Payment
	    #res = payment.mobile_checkout(product_name: productName, phone_number: str, currency_code: str, amount: float, metadata: dict = {}):
	    res = payment.mobile_checkout(product_name=productName, phone_number=chargephone, currency_code=currencyCode, amount=amount, metadata=metadata)
	    #print(res.get('status'))
	    print(res)
	    if(res.get('status') == 'PendingConfirmation'):
	    	print('moving to pay airtime function')
	    	pay(phone, amount)
	    	stats = Athist(amount=amount,status="sent", destination=phone,source=chargephone)
	    	stats.save()
	    	res=print(stats)
	    	return redirect('athistory')
	    else:
	    	print('No money')
	    return redirect('athistory')

@login_required
def buy(request):
	if request.method == "POST":
		amount = request.POST.get('amount')
		phone = request.POST.get('phone')
		pay(phone, amount)
		stats = Buyhist(amount=amount,status="sent", destination=phone)
		stats.save()
		return redirect('buyhistory')
	else:
		return render(request,'airtime/buy.html')


@login_required
def buy1(request):
	return render(request,'airtime/buy1.html')


@login_required
def rm(request,id):
	if request.method == "GET":
		print(id)
		d = Bulkhist.objects.get(id=id)
		d.delete()
		return redirect('bulkhist')
	else:
		return redirect('bulkhist')


@login_required
def delit(request,id):
	if request.method == "GET":
		print(id)
		d = Athist.objects.get(id=id)
		d.delete()
		return redirect('athistory')
	else:
		return redirect('athistory')




@login_required
def delete(request,id):
	if request.method == "GET":
		print(id)
		d = Buyhist.objects.get(id=id)
		d.delete()
		return redirect('buyhistory')
	else:
		return redirect('buyhistory')



	



	    