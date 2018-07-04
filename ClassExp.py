class Car:

    def _init_(self, x):
        self.xyz = x

    def turn_left(self, x):
        self.x = x


var = Car(30)
print(var.xyz)