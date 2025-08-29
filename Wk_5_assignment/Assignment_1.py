# Assignment 1: Design Your Own Class

# Creating a base class called Smartphone
class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, model, storage, battery):
        self.brand = brand      # phone brand (e.g., Samsung, iPhone)
        self.model = model      # phone model
        self.storage = storage  # storage capacity
        self.battery = battery  # battery percentage
    
    # Method for making a call
    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact} 📞")
    
    # Method for charging the phone
    def charge(self, amount):
        self.battery += amount
        # Keep battery between 0% and 100%
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")

# Child class that inherits from Smartphone
class GamingPhone(Smartphone):
    # Constructor adds extra attribute (cooling_system)
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    
    # Overriding call() method → polymorphism
    def call(self, contact):
        print(f"{self.brand} {self.model} uses gaming mode to call {contact} 🎮📞")
    
    # Extra method for gaming
    def play_game(self, game):
        if self.battery > 20:  # check if enough battery
            print(f"Playing {game} smoothly with {self.cooling_system} cooling ❄️")
            self.battery -= 20  # playing reduces battery
        else:
            print(f"Battery too low to play {game}! ⚡")

# Creating objects (instances) of the classes
phone1 = Smartphone("Samsung", "S22", "128GB", 75)
phone2 = GamingPhone("Asus", "ROG 6", "256GB", 90, "Liquid Cooling")

# Testing the methods
phone1.call("Alice")
phone1.charge(15)

phone2.call("Bob")
phone2.play_game("PUBG")
phone2.charge(5)
