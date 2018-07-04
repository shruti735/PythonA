
def drive(carspeed):
	if carspeed>200:
		print("very fast")
	elif carspeed>100:
		print("toofast")
	elif carspeed>70 and carspeed<80:
		print("optimal speed")
	else:
		print("below speed limit")
print(drive(234))
print(drive(34))
drive(134)
