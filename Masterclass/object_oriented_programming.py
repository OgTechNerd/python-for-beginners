# Object oriented python
# creating sample class

class vehicle(object):
    variable1 = "This is class variable, anyone can access from class"

    # This is default constructor
    def __init__(self, manufacturer, model, price, horsepower):
        self.model = model
        self.price = price
        self.horsepower = horsepower
        self.manufacturer = manufacturer
        self.gear = False
    
    @classmethod
    def familycar(cls):
        return cls("honda", "i10", 9000, 200)
    @classmethod
    def sportscar(cls):
        return cls("lamborghini", "hur", 100000000, 15000)
    


    # This is  not a class method
    def milage(self):
        if (self.horsepower >= 1000):
            print( "Mileage will be poor")
        else:
            print( "Mileage will be good")

if __name__ == "__main__":
    car1 = vehicle('ford', 'gt', 2000000, 800)
    print(car1.model);
    print(vehicle.variable1)
    print(car1.variable1)
    print(car1.milage())
    car2 = vehicle.sportscar()
    print(car2.milage())