from django.shortcuts import render
from django.shortcuts import redirect
import africastalking
from django.contrib import messages
import codecs
import re
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
def pcsv_download(request): 
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
		
		#split at line end
		rowz = re.split('\n', file_data)
		

		#what I want
		required_data = [elem for elem in rowz[1:]]
		recipients = []		
		for user in required_data:
			user_items = re.split(',',user)
			if len(user_items)>1:
				recipient = {}
				recipient['name']= user_items[0]
				recipient['phoneNumber'] = "+256"+user_items[1]
				recipient['currencyCode'] = "UGX"
				recipient['amount'] = user_items[2]
				recipient['reason'] = "SalaryPaymentWithWithdrawalChargePaid"
				recipient['metadata'] = {}
				recipients.append(recipient)				
			else:
				pass		
        
        #send
		sand_key ="db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		if len(recipients)<=10:
			africastalking.initialize(username='sandbox', api_key=sand_key)
			payment = africastalking.Payment
			res = payment.mobile_b2c(product_name='0zz', consumers=recipients)
			print(res)
			#save history
			user = []
			#for user in rowz[1:]:
				#hist=Bulkpayhist(name=user[0],amount="UGX"+user[2],status="successful",destination="+256"+user[1])
				#hist.save()
		else:
			new_dict_list = [recipients[i:i+10] for i in range(0,len(recipients),10)]
			recipient=[]
			#send to each group
			for recipient in new_dict_list:
				africastalking.initialize(username='sandbox', api_key=sand_key)
				payment = africastalking.Payment
				res = payment.mobile_b2c(product_name='0zz', consumers=recipient)
				#save history
				user = []
				#for user in new_list:
					#hist=Bulkpayhist(name=user[0],amount="UGX"+user[2],status="successful",destination="+256"+user[1])
					#hist.save()
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
        


#deletes here
#bulkpay table delete
@login_required
def del_hist(request):
	if request.method == "GET":
		drop_hist = Bulkpayhist.objects.all()
		drop_hist.delete()
		return redirect('bulkpayhist')
	else:
		return redirect('bulkpayhist')

#bulkpay item delete
@login_required
def del_item(request,id):
	if request.method == "GET":
		id_match = Bulkpayhist.objects.get(id=id)
		id_match.delete()
		messages.add_message(request, messages.INFO, 'Item Deleted')
		return redirect('bulkpayhist')
	else:
		return redirect('bulkpayhist')

#deposits table delete
@login_required
def deposits_del(request):
	if request.method == "GET":
		drop_hist = Payhist.objects.all()
		drop_hist.delete()
		return redirect('phistory')
	else:
		return redirect('phistory')

#deposits item delete
@login_required
def del_deposit(request,id):
	if request.method == "GET":
		id_match = Payhist.objects.get(id=id)
		id_match.delete()
		messages.add_message(request, messages.INFO, 'Item Deleted')
		return redirect('phistory')
	else:
		return redirect('phistory')


