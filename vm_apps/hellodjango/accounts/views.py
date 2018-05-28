from django.shortcuts import render, redirect
from django.contrib import auth, messages

# Create your views here.

def login(request):
	if request.method == "GET":
		#load the login form
		return render(request, "accounts/login.html")
	elif request.method == "POST":
		#process the form, authenticate the user 
		username = request.POST.get('uname')
		password = request.POST.get('psw')
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('home')
		else:
			messages.success(request, 'username or password is incorrect, Please try again')
			return redirect('login')

def home(request):
	return render(request, "accounts/home.html")