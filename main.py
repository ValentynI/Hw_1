class Plane:
    def __init__(self, fuel, maxspeed):
        self.fuel = fuel
        self.maxspeed = maxspeed
        def refuel(self, amount):
            self.fuel += amount
        def drive(self):
            if self.fuel > 0:
                print('Driving')
                self.fuel -= 1
            else:
                print("No fuel")
F16 = Plane(100, 400)
print(F16.fuel)
print(F16.maxspeed)
F22 = Plane(150, 660)
print(F22.fuel)
print(F22.maxspeed)
print('-------------------')
print(F16.fuel)
F16.refuel(10)
print(F16.fuel)
print('-------------------')
print(F22.fuel)
F22.drive()
print(F22.fuel)