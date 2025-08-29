# Activity 2: Polymorphism Challenge

# Base class Vehicle
class Vehicle:
    def move(self):
        # Abstract method → must be overridden by subclasses
        raise NotImplementedError("Subclass must implement this method")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Polymorphism in action:
# Same method name (move), but each class has its own behavior
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()   # Each object calls its own version of move()
