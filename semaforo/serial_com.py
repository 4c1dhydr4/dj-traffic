# -*- coding: utf-8 -*-
import serial

def get_serial(port):
	# system = input('Windows o Linux? (w/l):')
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = port
	return ser


def send_data(ser, mjs):
	ser.write(mjs.encode())
	