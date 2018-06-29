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
	if request.method == "POST":
		sand_key ="db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		africastalking.initialize(username='sandbox', api_key=sand_key)
		payment = africastalking.Payment
		consumers = [
    {
    
      "name": "Bob Mwangi",
      "phoneNumber": "+254718769882",
      "currencyCode": "KES",
      "amount": 6766.88,
      "providerChannel": "1212",
      "reason": 'SalaryPayment',
      "metadata": {}
    }
]
		return redirect('phistory')
	else:
		return render(request, "payments/bulk_pay.html")

@login_required
def phistory(request):
	return render(request, 'payments/phist.html')

