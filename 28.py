class YourException(Exception):
	pass
try:
	1/0
except Exception as e:
	print("It have exception"+str(e))



