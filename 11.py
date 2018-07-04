class Car: #: for block
	 
	def __init__(self,name): #constructor&method def
		self.pas=name #self.pas make name global
	def turn_left(self,name):
		self.pas=name #says/depicts self as a instance variable and pas take instance variable
var=Car(10) #car is object, var is ref variable,first check where is init,0para const is call if no name written
print(var.pas)


class MyClass:
 
 	def __init__(self, Name="there"):
  		self.Greeting = Name + "!"
	def SayHello(self):
 		print("Hello {0}".format(self.Greeting))

var=MyClass()
print(var.Greeting)
