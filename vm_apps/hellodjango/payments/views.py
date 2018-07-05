from django.shortcuts import render
from django.shortcuts import redirect
import africastalking
import codecs
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Payhist
from .models import Bulkpayhist
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

		#consumer
		recipient = [{
		"name": name,
        "phoneNumber": phoneNumber,
        "currencyCode": currencyCode,
        "amount": amount,
        "reason": reason,
        "metadata": {}
    	}]
		
		#api call        
		sand_key ="db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		africastalking.initialize(username='sandbox', api_key=sand_key)
		payment = africastalking.Payment
		res = payment.mobile_b2c(product_name='0zz', consumers=recipient)
		
		#save history
		pay_hist=Payhist(name=name,amount=currencyCode+amount,status="successful",destination=phoneNumber)
		pay_hist.save()
		stats = Payhist.objects.all()
		#history
		return redirect('phistory')
	else:
		return render(request, "payments/index.html")


@login_required
def csv_download(request): 
	import csv

	""" Renders a csv list  """
	response = HttpResponse(content_type='csv')
	response['Content-Disposition'] = 'attachment; filename=sample.csv'
	writer = csv.writer(response, dialect=csv.excel)
	writer.writerow(['Name', 'Contact','Amount'])
	writer.writerow(['receiver_1', 'Contact_1','Amount_1'])
	writer.writerow(['receiver_2', 'Contact_2','Amount_2'])
	print(response)
	return response


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
		mo = file_data.split('\n')
		lines = file_data.split(',')



		file_reader = csv.reader(file_data, delimiter=',')
		#for  row in file_reader:
			#first_row=row[0]
			#print()


		#first line
		rows = lines[:3]
		rs = mo[1:]

		#skip first line
		r = [elem for elem in lines if elem not in set(rs) ]
		print(lines)

		
		#skip first 3 and "\n"		
		row_data = [elem for elem in lines if elem not in set(rows)]
		var_x = [row for row in mo if row not in set(rs) ]
		
		#group into 3s
		new_list = [var_x[i:i+3] for i in range(0, len(var_x), 3)]
		user_dict_list = []

		print(rows)

		for user_list in new_list:
			user_dict = {}
			user_dict['name'] = "".join(user_list[0])
			user_dict['phoneNumber'] = "+256"+user_list[1]
			user_dict['currencyCode'] = "UGX"
			user_dict['amount'] = user_list[2]			
			user_dict['reason'] = "SalaryPaymentWithWithdrawalChargePaid"
			user_dict['metadata'] = {}			
			user_dict_list.append(user_dict)				
		
		sand_key ="db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		
		if len(user_dict_list)<=10:
			africastalking.initialize(username='sandbox', api_key=sand_key)
			payment = africastalking.Payment
			res = payment.mobile_b2c(product_name='0zz', consumers=user_dict_list)
			#save history
			user = []
			for user in new_list:
				hist=Bulkpayhist(name=user[0],amount="UGX"+user[2],status="successful",destination="+256"+user[1])
				hist.save()			

		else:
			#group list into 10z
			new_dict_list = [user_dict_list[i:i+10] for i in range(0,len(user_dict_list),10)]
			recipient=[]
			#send to each group
			for recipient in new_dict_list:
				africastalking.initialize(username='sandbox', api_key=sand_key)
				payment = africastalking.Payment
				res = payment.mobile_b2c(product_name='0zz', consumers=recipient)
				#save history
				user = []
				for user in new_list:
					hist=Bulkpayhist(name=user[0],amount="UGX"+user[2],status="successful",destination="+256"+user[1])
					hist.save()
		#history
		return redirect('bulkpayhist')
	else:
		return render(request, "payments/bulk_pay.html")

@login_required
def phistory(request):
	users = Payhist.objects.all()
	return render(request, 'payments/phist.html',{"users":users})

@login_required
def bulkpayhist(request):
	if request.method == "POST":
		stats = Bulkpayhist.objects.order_by("-date")
		return render( request,"payments/bulkpayhist.html",{"stats":stats})
	else:
		stats = Bulkpayhist.objects.order_by("-date")
		page = request.GET.get('page', 1)
		paginator = Paginator(stats, 15)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
		
		return render( request,"payments/bulkpayhist.html",{"users":users})


@login_required
def schedule_pay(request):
	return render(request, 'payments/schedule_pay.html')
        
