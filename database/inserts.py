import sqlite3
import datetime


def open_db():
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	return conn, c

def close_db(conn, c):
	c.close()
	conn.close()

def insert_event(camera, cars, state, duration, numCambios):
	conn, c = open_db()
	now = datetime.datetime.now()
	now = now.strftime('%Y-%m-%d %H:%M:%S')
	c.execute("INSERT INTO traffic_event (date,cars,status,duration,changesNumber,camera_id) VALUES('{}',{},{},{},{},{})".format(now,cars,state,duration,numCambios,camera))
	conn.commit()
	close_db(conn, c)