# Exercise 14:

class Vehicle:
    def __init__(self, fuel_level, kilometers_driven, name, number_of_wheels=4):
        self.number_of_wheels = number_of_wheels
        self.fuel_level = fuel_level
        self.kilometers_driven = kilometers_driven
        self.name = name

    def need_inspection(self):
        return self.kilometers_driven >= 1000

    def drive(self, kilometers_to_drive):
        self.kilometers_driven += kilometers_to_drive
        self.fuel_level -= (kilometers_to_drive / 100) * 10

        if self.fuel_level <= 0:
            print("Out of fuel. Refuel first.")
            self.kilometers_driven -= kilometers_to_drive  # Rollback the kilometers driven update
            return

        if self.need_inspection():
            self.do_inspection()

    def honk(self):
        print("Tut tut")

    def refuel(self, fuel_amount):
        self.fuel_level += fuel_amount

    def do_inspection(self):
        print(f"Vehicle {self.name} needs inspection.")
        # Perform inspection tasks here

    def obd(self):
        print(f"Status Report for {self.name}:")
        print(f"Number of Wheels: {self.number_of_wheels}")
        print(f"Fuel Level: {self.fuel_level} liters")
        print(f"Kilometers Driven: {self.kilometers_driven}")
        if self.need_inspection():
            print("Inspection Required")
        else:
            print("No Inspection Required")


# Test Scenario
car = Vehicle(fuel_level=50, kilometers_driven=0, name="MyCar")

for _ in range(15):
    car.drive(80)
    car.honk()
    car.obd()

    if car.fuel_level <= 10:
        car.refuel(30)

    if car.need_inspection():
        car.do_inspection()