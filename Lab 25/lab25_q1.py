class Car:
    # Class attribute
    showroom = "NewAge"

    def __init__(self, make, model, year, color, started=False, speed=0, max_speed=200):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = started
        self.speed = speed
        self.max_speed = max_speed

    # Class method to change the showroom name
    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name

    # Magic method to define the string representation of an object
    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    # Static method to display an introductory message
    @staticmethod
    def show_intro_message():
        print("The Car class represents cars and their properties.")


# (a) Create the Toyota Camry instance
toyota_camry = Car("Toyota", "Camry", 2022, "Red")

print("PART (a): Toyota Camry")
print("Make:", toyota_camry.make)
print("Model:", toyota_camry.model)
print("Year:", toyota_camry.year)
print("Color:", toyota_camry.color)
print("Started:", toyota_camry.started)
print("Speed:", toyota_camry.speed)
print("Maximum Speed:", toyota_camry.max_speed)


# (b) Create the Ford Mustang instance
ford_mustang = Car("Ford", "Mustang", 2022, "Black")

print("\nPART (b): Ford Mustang")
print("Make:", ford_mustang.make)
print("Model:", ford_mustang.model)
print("Year:", ford_mustang.year)
print("Color:", ford_mustang.color)
print("Started:", ford_mustang.started)
print("Speed:", ford_mustang.speed)
print("Maximum Speed:", ford_mustang.max_speed)


# (c) Accessing an attribute through the class
print("\nPART (c): Accessing Class Attributes")

try:
    print(Car.make)
except AttributeError as e:
    print("Error:", e)

print("Toyota make:", toyota_camry.make)
print("Ford make:", ford_mustang.make)


# (d) Display the class dictionary
print("\nPART (d): Car.__dict__")
print(Car.__dict__)


# (e) Change the showroom name using the class method
print("\nPART (e): Class Attribute - Showroom")
print("Original showroom:", Car.showroom)

Car.change_showroom("Luxury Motors")

print("Updated showroom:", Car.showroom)
print("Updated Car.__dict__:", Car.__dict__)


# (f) Display the instance dictionary
print("\nPART (f): toyota_camry.__dict__")
print(toyota_camry.__dict__)


# (g) Test the __str__ magic method
print("\nPART (g): String Representation")
print(str(toyota_camry))
print(str(ford_mustang))


# (h) Call the static method
print("\nPART (h): Static Method")
Car.show_intro_message()


## Explanation of Each Part

### (a) Create the `toyota_camry` instance

toyota_camry = Car("Toyota", "Camry", 2022, "Red")
