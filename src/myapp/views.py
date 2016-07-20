from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NewsForm, NewsModelForm
from .models import NewsSignUp


# Create your views here.
def home(request):
	form = NewsModelForm(request.POST or None)

	# if request.method == "POST":
	# 	print request.POST
	# 	print request.POST.get("email")

	if form.is_valid():
		instance = form.save(commit=False)
		email2 = form.cleaned_data.get("email2")
		print email2
		instance.save()
		# user_nombre = form.cleaned_data.get("nombre")
		# user_email = form.cleaned_data.get("email")
		# obj = NewsSignUp.objects.create(nombre=user_nombre, email=user_email)
		return HttpResponseRedirect("/home/")	
	# 	print form.cleaned_data
	# 	print form.cleaned_data.get("email")

	# if not form.is_valid():
	# 	print form.errors
		

	context = {
		"form": form
	}


	return render(request, "form.html", context)