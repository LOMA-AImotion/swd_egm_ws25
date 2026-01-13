class Car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour
    
    def print_info(self):
        info_str = f"Car brand: {self.brand}, Model: {self.model}, Colour: {self.colour}"
        print(info_str)


class CityCar(Car):
    def __init__(self, brand, model, colour, emission_class):
        super().__init__(brand, model, colour)
        self.emission_class = emission_class
        
    def print_info(self):
        info_str = f"Car brand: {self.brand}, Model: {self.model}, Colour: {self.colour}, Emission class: {self.emission_class}"
        print(info_str)


car1 = Car("Audi", "A3", "silver")
car2 = Car("BMW", "5", "blue")

car3 = CityCar("Smart", "ForTwo", "red", "Green")
 
print(car1.brand)
print(car2.brand)

print(car3.emission_class)

car1.print_info()
car2.print_info()
car3.print_info()