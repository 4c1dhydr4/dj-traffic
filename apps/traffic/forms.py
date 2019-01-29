from django import forms
from apps.traffic.models import Camera

class CameraForm(forms.ModelForm):
	class Meta:
		model = Camera
		fields = (
			'ip',
			'orientation',
			'location',
			'url',
			'active',
		)
		labels = {
			'ip':'Dirección IP',
			'orientation':'Orientación',
			'location':'Locación',
			'url':'URL de Acceso',
			'active':'Cámara Activa',
		}
		widgets = {
			'ip': forms.TextInput(attrs={'class':'form-control'}),
			'orientation': forms.Select(attrs={'class':'form-control'}),
			'location': forms.TextInput(attrs={'class':'form-control'}),
			'url': forms.TextInput(attrs={'class':'form-control'}),
			'active': forms.CheckboxInput(),
		}