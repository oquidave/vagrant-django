from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Fwno
# Create your views here.
def index(request):
	return render(request, "voice/index.html")

def fwd(request):
	if "POST" == request.method:
		#get no
		number=request.POST.get('addno')
		print(number)
		
		#save no
		stats=Fwno(num=number)
		stats.save()
		print(stats)
		return redirect('fwd')
	elif "GET" == request.method:
		stats=Fwno.objects.all()
		return render(request,'voice/fwd.html',{'stats':stats})

def vhistory(request):
	return render(request, "voice/vhist.html")

def make_call(request):
	return HttpResponse("Make a voice call.")


def delete(request,id):
	if request.method == "GET":
		print(id)
		d = Fwno.objects.get(id=id)
		d.delete()
		return redirect('fwd')
	else:
		return redirect('fwd')

