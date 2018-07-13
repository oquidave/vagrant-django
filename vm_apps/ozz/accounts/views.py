from django.shortcuts import render, redirect
from django.contrib import auth, messages
from accounts.decorators import logout_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	if request.user.is_authenticated():
		return redirect('dashboard')
	else:
		return redirect('signup')

#@logout_required
def login(request):
	if request.method == 'GET':
		logout(request)
		return render(request, 'accounts/login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return redirect('dashboard')
	else:
		messages.success(request, 'username or password is wrong')
		return redirect('login')

#@logout_required
def signup(request):
	if request.method == 'GET':
		logout(request)
		return render(request, 'accounts/signup.html')
	else:
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		password = request.POST.get('password')
		user = User.objects.create_user(username = username,
										first_name = first_name,
										last_name = last_name,
		 								email = email,		 								
		 								password = password)	
		user.save()
		if user.pk:
			messages.success(request, 'registration was successful')
			return redirect('login')
		else:
			messages.success(request, 'registration was failed')
			return redirect('signup')

def profile(request):
	if request.method == 'GET':
		return render(request, 'accounts/profile.html')
	else:
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = request.user
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.password = password
		user.save()
		messages.success(request, 'profile has been saved')
		return redirect('profile')

