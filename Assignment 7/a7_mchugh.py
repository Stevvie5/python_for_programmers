# Thomas McHugh 

##Write your code for part 1 BELOW THIS LINE 
class Vehicle(object):
	def __init__(self, mode, maxPassengers=1, odometer=0):
		'Instantiates the Vehicle class'
		self.mode = mode
		self.maxPassengers = maxPassengers
		self.odometer = odometer
		
	def odometerAdd(self, quantity):
		'Adds a quantity to the odometer'
		self.odometer += quantity
	
	def __str__(self):
		'Returns general information about the vehicle'
		return "The mode of transport is: {0}\nCan carry up to: {1}\nOdometer: {2}".format(self.mode, self.maxPassengers, self.odometer)
		
	def __eq__(self, otherVehicle):
		'Checks to see if another vehicle is identical to the current vehicle'
		if self.odometer != otherVehicle.odometer:
			return False
		elif self.mode != otherVehicle.mode:
			return False
		elif self.maxPassengers != otherVehicle.maxPassengers:
			return False
		
		return True
		
class Car(Vehicle):
	def __init__(self, mode, maxPassengers, odometer, make, model, color):
		'Instantiates the Car class'
		super().__init__(mode, maxPassengers, odometer)
		
		self.make = make
		self.model = model
		self.color = color
		
	def __str__(self):
		'Returns general information about the car'
		return super().__str__() + '\nMake: {0}\nModel: {1}\nColor: {2}'.format(self.make, self.model, self.color)
		
	def __eq__(self, otherCar):
		'Checks to see if another car is identical to the current car'
		inheritCheck = super().__eq__(otherCar)
		if inheritCheck == False:
			return False
		elif self.make != otherCar.make:
			return False
		elif self.model != otherCar.model:
			return False
		elif self.color != otherCar.color:
			return False

		return True

class Boat(Vehicle):
	def __init__(self, mode, maxPassengers=1, odometer=0, length=0, horsepower=0):
		'Instantiates the Boat class'
		super().__init__(mode, maxPassengers, odometer)
		
		self.length = length
		self.horsepower = horsepower
		
	def __str__(self):
		'Returns general information about the boat'
		return super().__str__() + '\nLength: {0}\nHorsepower: {1}'.format(self.length, self.horsepower)
		
	def __eq__(self, otherBoat):
		'Checks to see if another boat is identical to the current boat'
		inheritCheck = super().__eq__(otherBoat)
		if inheritCheck == False:
			return False
		elif self.length != otherBoat.length:
			return False
		elif self.horsepower != otherBoat.horsepower:
			return False

		return True
		
'''
Explanation of Super

The super function is used within a class to get access to the methods that are a part of the inherited class. It should be used when you want to not just override a method that exists in the inherited class but want to run the method from the inherited class and then run additional code. For example, the Boat class is inherited by the Vehicle class. In the constructor of the Vehicle class, the variables for mode, max passengers, and odometer are set. We want these variable to continue to be set in our Boat class, so instead of just defining the constructor and having to manually retype the code that runs in the Vehicle constructor, we can run the constructor method for Vehicle inside the Boat class constructor and then write additional code that could define specific logic or define new variable pertinent to the Boat class.

It is quite a good idea to use the super function because often times classes that inherit another class are using the inherited class as a foundation for the new class. When you build a house, you build on top of the foundation, not next to the foundation. Super and class inheritance is the same way. Often times we need to run the method of the inherited class and then do something more that differentiated the new class method from the inherited class method. Without using super we would need to re-write the entire method from the inherited which would make inheritance almost pointless. With super, you just need one line to run the entire inherited method inside the new class's method.
'''

## Tests
## FEEL FREE TO UNCOMMENT THIS SECTION IF YOU WITH TO TEST ##
## Remember that you can highlight a section and type ALT-4 to uncomment


##v = Vehicle("air", 50, 14000)
##print("created vehicle instance")
##print("Running __str__ for vehicle")
##print(v)
##print()
##
##c1 = Car("ground", 5, 15000, "toyota", "camry", "red")
##print("created car (c1) instance")
##print("Running __str__ for car")
##print(c1)
##print()
##
##c2 = Car("ground", 7, 39000, "dodge", "caravan", "blue")
##print("created car (c2) instance")
##print("Running __str__ for car")
##print(c2)
##print()
##
##print("checking c1 == c2:")
##print(c1 == c2)
##print()
##
##print("testing odometerAdd(789)...")
##c2.odometerAdd(798)
##print(c2)
##print()
##
##b1 = Boat("water", 10, 10000, 15, 360)
##print("created boat (b1) instance")
##print("Running __str__ for boat")
##print(b1)
##print()
##
##b2 = Boat("water", 10, 10000, 15, 360)
##print("created boat (b2) instance")
##print("Running __str__ for boat")
##print(b2)
##print()
##
##print("checking if b1 == b2")
##print(b1 == b2)
