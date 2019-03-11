import a7_mchugh as a

v = a.Vehicle("air", 50, 14000)
print("created vehicle instance")
print("Running __str__ for vehicle")
print(v)
print()

c1 = a.Car("ground", 5, 15000, "toyota", "camry", "red")
print("created car (c1) instance")
print("Running __str__ for car")
print(c1)
print()

c2 = a.Car("ground", 7, 39000, "dodge", "caravan", "blue")
print("created car (c2) instance")
print("Running __str__ for car")
print(c2)
print()

print("checking c1 == c2:")
print(c1 == c2)
print()

print("testing odometerAdd(789)...")
c2.odometerAdd(798)
print(c2)
print()

b1 = a.Boat("water", 10, 10000, 15, 360)
print("created boat (b1) instance")
print("Running __str__ for boat")
print(b1)
print()

b2 = a.Boat("water", 10, 10000, 15, 360)
print("created boat (b2) instance")
print("Running __str__ for boat")
print(b2)
print()

print("checking if b1 == b2")
print(b1 == b2)