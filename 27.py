class YourException(Exception):
	pass
try:
	raise YourException("dsghj")
except YourException as e:
	print("run"+str(e))



