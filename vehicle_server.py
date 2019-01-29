# -*- coding: utf-8 -*-
import cv2
import time
from semaforo.algorithms import get_light_code, get_direction, delay_normal, delay_longer
from semaforo.serial_com import get_serial, send_data
from database.inserts import insert_event

# from datetime import datetime

# print(cv2.__version__)


#Video Source
video_src1 = 'vid/vertical.mp4'
video_src2 = 'vid/horizontal.mp4'
cap1 = cv2.VideoCapture(video_src1)
cap2 = cv2.VideoCapture(video_src2)

"""
# IP Camera Source
host1 = '192.168.1.26'
host2 = '192.168.1.26'
cap1 = cv2.VideoCapture('http://'+host1+':8080/video')
cap2 = cv2.VideoCapture('http://'+host2+':8080/video')

"""

ip_vertical = 1 #'192.168.1.26'
ip_horizzontal = 3 #'192.168.1.27'

ser = get_serial('COM4')

cascade_src = 'semaforo/cars_neural_network.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

"""
Configuración inicial el semáforo
"""
if not ser.is_open:
	ser.open()
print("Configurando estado inicial del semáforo")
time.sleep(5)
light_stat = False #False = Vertical, True = Horizontal
msj, state = get_light_code(0, 0, 0, 0)
send_data(ser,msj)
time.sleep(3)
#Tiempo Inicial
time_one = time.time()

numCambios = 0

while True:
	# time.sleep(2) #Para Pruebas de videos cortos
	#Captura cuadro por cuadro en cáda iteración
	ret1, img1 = cap1.read()
	if (type(img1) == type(None)):
		break #Sale del bucle cuando termine el video

	ret2, img2 = cap2.read()
	if (type(img2) == type(None)):
		break
	
	#Se transforma a escala de grises para reducir trabajo de cómputo
	gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	
	#Detectas los vehículos utilizando redes neuronales
	cars1 = car_cascade.detectMultiScale(gray1, 1.1, 1)
	cars2 = car_cascade.detectMultiScale(gray2, 1.1, 1)

	#Para utilizar la imagen sin escala de grises
	# cars1 = car_cascade.detectMultiScale(img1, 1.1, 1)
	# cars2 = car_cascade.detectMultiScale(img2, 1.1, 1)
	
	#Cuenta de carros se resetea en cada iteración
	sv = 0
	sh = 0

	#Se realiza la cuenta de autos y se dibuja un rectángulo en cada auto
	for (x,y,w,h) in cars1:
		sv = sv + 1
		cv2.rectangle(img1,(x,y),(x+w,y+h),(255,255,255),1)

	for (x,y,w,h) in cars2:
		sh = sh + 1
		cv2.rectangle(img2,(x,y),(x+w,y+h),(255,255,255),1)

	#Se Calcula la diferencia entre timepo inicial y tiempo final
	interval_between_times = time.time() - time_one
	#De a cuerdo al tiempo largo se toma la decición de cambiar los semáforos
	state_before = state
	if interval_between_times >= delay_normal:
		msj, state = get_light_code(state, interval_between_times, sv, sh)
		if state != -1:
			numCambios = numCambios + 1
			direction = get_direction(state)
			interval_between_times = interval_between_times
			print("V: {} - H: {} - Estado: {} - Tiempo: {}".format(sv,sh,direction,interval_between_times,numCambios))
			insert_event(ip_vertical,sv,direction,interval_between_times,numCambios)
			insert_event(ip_horizzontal,sh,direction,interval_between_times,numCambios)
			send_data(ser,msj)
			time_one = time.time()
		else:
			state = state_before

	cv2.imshow('Cam Vertical', img1)
	cv2.imshow('Cam Horizontal', img2)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
ser.close()