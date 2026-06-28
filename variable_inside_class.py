class Car:
    # 1. CLASS VARIABLE (Shared by all cars)
    wheels = 4

    def __init__(self, brand, model):
        # 2. INSTANCE VARIABLES (Unique to each car)
        self.brand = brand
        self.model = model

# Create two distinct objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

# Accessing Instance Variables (They are different)
print(car1.brand)  # Output: Toyota
print(car2.brand)  # Ou tput: Tesla

# Accessing Class Variables (They share the same value)
print(Car.wheels)   # Output: 4 (Accessed via Class Name)
print(car1.wheels)  # Output: 4 (Accessed via Instance)
print(car2.wheels)  # Output: 4 (Accessed via Instance)