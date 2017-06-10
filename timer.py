#!/usr/bin/python

from threading import Timer

set_time = int(input('Enter time in seconds: '))

def message():
	print("Time up!!!, stop now!!")

t = Timer(set_time, message)

print("Timer Started...")

t.start()
