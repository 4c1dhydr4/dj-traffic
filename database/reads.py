import sqlite3
import datetime


def open_db():
	conn = sqlite3.connect('semaforo.db')
	c = conn.cursor()
	return conn, c

def close_db(conn, c):
	c.close()
	conn.close()

def read_event(cam):
	conn, c = open_db()
	c.execute('SELECT * FROM Evento WHERE camara_id={}'.format(cam))
	data = c.fetchall()
	event = data[-1]
	close_db(conn,c)
	return event