
from django.shortcuts import redirect


def logout_required(view_func):
	def _wrapped_view_func(request, *args, **kwargs): 
		if request.user.is_authenticated:
			return redirect('logout')
		else:
			return view_func(request, *args, **kwargs)
		return _wrapped_view_func
	return _wrapped_view_func