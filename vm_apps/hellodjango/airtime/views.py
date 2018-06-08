from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import africastalking
from ATLib.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# Create your views here.
def index(request):
	return render(request, "airtime/index.html")

def send_airtime(request):
    return HttpResponse("Send Airtime ")


def era(request):
	return render(request,'airtime/era.html')


def xs(request):
	return render(request,"airtime/xs.html")

def athistory(request):
	return render(request,'airtime/athist.html')


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
	    else:
	    	print('No money')
	    return render(request,'airtime/xs.html')

	    #return render('airtime/pay.html')