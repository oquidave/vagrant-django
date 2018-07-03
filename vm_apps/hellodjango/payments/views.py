from django.shortcuts import render
from django.shortcuts import redirect
import africastalking
import codecs
import csv
from django.http import HttpResponse
from .models import Payhist
from .models import Csv_data
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
	data = {}
	if request.method == "POST":
		#get name
		name = request.POST.get("receiver_name")
		
		#get number
		phoneNumber = request.POST.get("receiver_no")

		#get amount
		amount = request.POST.get("amount")
		
		#reason
		reason = request.POST.get("mm_reason")

		meta = {}

		currencyCode = "UGX"

		#consumers
		recipient = [{
		"name": name,
        "phoneNumber": phoneNumber,
        "currencyCode": currencyCode,
        "amount": amount,
        "reason": reason,
        "metadata": {}
    	}]
		        
		print(recipient)

		sand_key ="db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		africastalking.initialize(username='sandbox', api_key=sand_key)
		payment = africastalking.Payment
		res = payment.mobile_b2c(product_name='0zz', consumers=recipient)
		print(res)
		#save history
		pay_hist=Payhist(name=name,amount=currencyCode+amount,status="successful",destination=phoneNumber)
		pay_hist.save()
		stats = Payhist.objects.all()
		print(stats)
		return redirect('phistory')
	else:
		return render(request, "payments/index.html")


@login_required
def bulk_pay(request):
	data = {}
	if request.method == "POST":
		#get file content
		csv_file = request.FILES["receiver"]

		#reason
		reason = request.POST.get("mm_reason")

		#read into file
		file_data = csv_file.read().decode("utf-8")
		
		#split into lines//make list
		lines = file_data.split(',')
		
		#first 3
		rows = lines[:3]
		
		#skip rows
		row_data = [elem for elem in lines if elem not in set(rows)]
		var_x = [row for row in row_data if row != "\n"]
		#print(var_x)
		
		#filter out '\n' and join values
		#clean_data =",".join([elem for elem in row_data if elem !="\n"])

		#group into 3s
		new_list = [var_x[i:i+3] for i in range(0, len(var_x), 3)]
		names = [item[0] for item in new_list]
		number = [item[1] for item in new_list]
		amount = [item[2] for item in new_list]
		print(names[0])
		#print(type(rows))		
		sand_key ="db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		africastalking.initialize(username='sandbox', api_key=sand_key)
		payment = africastalking.Payment
		res = payment.mobile_b2c(product_name='0zz', consumers=consumers)
		print(res)
		return redirect('phistory')
	else:
		return render(request, "payments/bulk_pay.html")

@login_required
def phistory(request):
	users = Payhist.objects.all()
	return render(request, 'payments/phist.html',{"users":users})

@login_required
def schedule_pay(request):
	return render(request, 'payments/schedule_pay.html')
        
