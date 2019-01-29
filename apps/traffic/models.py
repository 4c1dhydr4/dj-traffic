from django.db import models

class Camera(models.Model):
	ORIENTACION = (
		('Vertical','Vertical'),
		('Horizontal','Horizontal'),
	)

	ip = models.CharField(max_length=20, blank=False, help_text="Ingrese la IP estática de la Cámara")
	orientation = models.CharField(max_length=20, blank=False, choices=ORIENTACION,help_text="Ingrese la Orientación según coordenadas (Ejemplo: Vertical)") 
	location = models.CharField(max_length=50, blank=False, help_text="Locación exacta de la Cámara")
	url = models.URLField(max_length=100, blank=False, help_text="URL de Acceso")
	active = models.BooleanField(default=False, help_text="Estado (Marcar para Activo)")

	def __str__(self):
		return '{}'.format(self.location)

class Event(models.Model):
	camera = models.ForeignKey(Camera, null=False, blank=False, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True, blank=False)
	cars = models.SmallIntegerField(null=False, blank=False)
	status =  models.BooleanField() #False: Rojo - True: Verde
	duration = models.DecimalField(max_digits=5,decimal_places=2,blank=False)
	changesNumber = models.SmallIntegerField(null=False, blank=False)

	def __str__(self):
		return '{} - {}'.format(self.date, self.camera)