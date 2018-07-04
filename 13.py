class Car: #: for block


	def __init__(self):
		self.x=60
		print("im from constructor")
	def turn_left(self,x):
		self.x=x
		print("im from turn left")
var=Car()
print(var.x)
print(var.turn_left(29))

