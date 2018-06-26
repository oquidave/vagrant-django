from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#from django.contrib import messages
from .models import Fwno
from lxml import etree

import africastalking
# Create your views here.
@login_required
def index(request):
	return render(request, "voice/index.html")

@login_required
def fwd(request):
	if "POST" == request.method:
		#get no
		number=request.POST.get('addno')
		#print(number)
		#sort
		b = Fwno.objects.all()
		#print(b)		
		#filter number
		x = b.filter(num=number)
		#print(x)
		if x:
			#if num already exists
			#print(number)
			mssg = "Number already exists in list"
			return HttpResponse(mssg, content_type='text/plain')			
		else:
			#if doesnt exist,save to model
			stats=Fwno(num=number)
			stats.save()
			#print(stats)
			return redirect('fwd')			
	elif "GET" == request.method:
		stats = Fwno.objects.all()
		return render(request,'voice/fwd.html',{'stats':stats})


def err(request):
	return render(request, "voice/err.html")


@login_required
def dial(request):
	if "GET" == request.method:
		nums = Fwno.objects.filter(num=num)
		api_key = "db76dc5eb626a86afb261dc1eb729a5bd6c4c1ea04b5cec23162ae36f24bf377"
		print(nums)
		africastalking.initialize(username='sandbox', api_key=api_key)
		voice = africastalking.Voice
		res = voice.dial(phone_number=nums)
		print(res)
		return redirect('vhistory')
	else:
		return redirect('fwd')
		


@login_required
def vhistory(request):
	return render(request, "voice/vhist.html")

#def make_call(request):
#	return HttpResponse("Make a voice call.")

@login_required
def delete(request,id):
	if request.method == "GET":
		print(id)
		d = Fwno.objects.get(id=id)
		d.delete()
		return redirect('fwd')
	else:
		return redirect('fwd')

@csrf_exempt
def make_call(request):
	# create XML 
	root = etree.Element('Response')
	child = etree.SubElement(root, 'Say', voice='man')
	child.text = 'some text for test'
	s = etree.tostring(root, pretty_print=True)
	#print(s)
	return HttpResponse(s, content_type="application/xml")


