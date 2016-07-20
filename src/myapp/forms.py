from django import forms

from .models import NewsSignUp

class NewsModelForm(forms.ModelForm):
	email2 = forms.EmailField(max_length=100)
	# codigo_postal =
	# direccion = 
	class Meta:
		model = NewsSignUp
		fields = ["nombre", "email"]

	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Los emails no coinciden. Vuelve a intentar.")
		return email2


	def clean(self, *args, **kwargs):
		form_email = self.cleaned_data.get("email")
		qs = NewsSignUp.objects.filter(email=form_email)
		if qs.exists():
			raise forms.ValidationError("Email ya existe. Prueba con otro por favor.")
		return super(NewsModelForm, self).clean(*args, **kwargs)


class NewsForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=50)
	email2 = forms.EmailField(max_length=50)

	# def clean_email2(self):
	# 	email = self.cleaned_data.get("email")
	# 	email2 = self.cleaned_data.get("email2")
	# 	if email != email2:
	# 		raise forms.ValidationError("Los emails no coinciden. Vuelve a intentar.")
	# 	return email2


	# def clean(self, *args, **kwargs):
	# 	form_email = self.cleaned_data.get("email")
	# 	qs = NewsSignUp.objects.filter(email=form_email)
	# 	if qs.exists():
	# 		raise forms.ValidationError("Email ya existe. Prueba con otro por favor.")
	# 	return super(NewsForm, self).clean(*args, **kwargs)