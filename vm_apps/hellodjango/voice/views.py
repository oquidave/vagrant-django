from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from lxml import etree
from .models import Fwno



import africastalking
# Create your views here.
@csrf_exempt
def kol(request):
	#get column "num"
	nums = Fwno.objects.values_list('num',flat=True)
	#make nums set
	y = set(nums)
	#join set into string
	x=','.join(nums)
	print(x)
	#get number
	number = request.POST.get('number')
	print(number)
	
	#create XML
	root = etree.Element('Response')
	child = etree.SubElement(root, 'Dial', phoneNumbers=x,sequential="true")
	s = etree.tostring(root, pretty_print=True)
	#print(s)
	return HttpResponse(s, content_type="application/xml")




@login_required
def index(request):
	return render(request,'voice/index.html')
	

@csrf_exempt
def fwd(request):
	if "POST" == request.method:
		#get no
		number=request.POST.get('addno')
		message = request.POST.get('mssg')
		
		#sort
		b = Fwno.objects.all()
		print(b)		
		#filter number
		x = b.filter(num=number)
		#print(x)
		if x:
			#if num already exists
			#print(number)
			messages.add_message(request, messages.INFO, 'number has already been added')
			return redirect('fwd')			
		else:
			#if doesnt exist,save to model
			stats=Fwno(num=number)
			stats.save()
			return redirect('fwd')
									
	elif "GET" == request.method:
		stats = Fwno.objects.all()
		return render(request,'voice/fwd.html',{'stats':stats})


def err(request):
	return render(request, "voice/err.html")



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
	#make xml
	root = etree.Element('Response')
	#create action and voice
	child = etree.SubElement(root, 'Say', voice='woman')
	#set text
	child.text = 'Hey, you ,have reached Mark,hold on for a moment, while  we linkie!'
	s = etree.tostring(root, pretty_print=True)
	#print(s)
	return HttpResponse(s, content_type="application/xml")
	





