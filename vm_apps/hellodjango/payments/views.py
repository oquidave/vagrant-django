from django.shortcuts import render
from django.shortcuts import redirect
import africastalking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
	return render(request, "payments/index.html")


@login_required
def bulk_pay(request):
	data = {}
	if request.method == "POST":
		#get file content
		file = request.FILES["receiver"]

		#reason
		reason = request.POST.get("reason")

		#read into file
		file_data = file.read().decode("utf-8")

		print(file_data)

		sand_key ="db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		africastalking.initialize(username='sandbox', api_key=sand_key)
		payment = africastalking.Payment
		res = payment.mobile_b2c(product_name='Ozz', consumers=consumers)
		print(res)
		return redirect('phistory')
	else:
		return render(request, "payments/bulk_pay.html")

@login_required
def phistory(request):
	return render(request, 'payments/phist.html')
        
