# -*- coding: utf-8 -*-
delay_normal = 5
delay_longer = 15


vertical_msj = "Vertical_PASS\n"
horizontal_msj = "Horizontal_PASS\n"
continue_msj = "Continue\n"

cars_normal = 2 #Conteo normal de vehículos

def state_conditions(state, delay, sv, sh):
	if state == 0:
		return 1
	else:
		if state == 1:
			if delay >= delay_longer:
				if sv == sh:
					return 2
				elif sv > sh:
					return 2
				elif sv < sh:
					if sv <= cars_normal:
						return -1
					else:
						return 2
			elif delay >= delay_normal:
				if sv == sh:
					return -1
				elif sv > sh:
					if sv > cars_normal:
						return 2
					else:
						return -1
				elif sv < sh:
					return -1
		elif state == 2:
			if delay >= delay_longer:
				if sv == sh:
					return 1
				elif sv > sh:
					if sv > cars_normal:
						return -1
					else:
						return 1
				elif sv < sh:
					return 1
			elif delay >= delay_normal:
				if sv == sh:
					return -1
				elif sv > sh:
					return -1
				elif sv < sh:
					if sv > cars_normal:
						return -1
					else:
						return 1
	return -1


def get_light_code(state, delay, sv, sh):
	msj = ""
	state = state_conditions(state, delay, sv, sh)
	if state == 1:
		msj = horizontal_msj
	if state == 2:
		msj = vertical_msj
	if state == -1:
		msj = continue_msj
	return msj, state

def get_direction(state):
	msj = ""
	if state == 1:
		msj = 0
	elif state == 2:
		msj = 1
	return msj
