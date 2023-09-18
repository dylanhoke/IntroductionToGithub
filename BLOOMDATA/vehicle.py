
'''
This file holds two classes: Vehicle and Convertible that are parent and child classes respectibly
'''
#imagine i want to list these vehicles on craigslist
#parent class i smore generic of the two classes
class Vehicle:
    def __init__(self,make,model,color,year,mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
    def honk(self):
        return "HOOOOOOOOOOOOOOOONK!"
    def drive(self,miles_driven):
        self.mileage +=  miles_driven
        return self.mileage
    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles"
# if __name__ == "__main__":
#     my_vehicle = Vehicle("Toyota","Camry","gray",2015,60000)

#     print(my_vehicle.make)
#     print(my_vehicle.mileage)
#     print(my_vehicle.honk())
#     print(my_vehicle.drive(1234))
#     print(my_vehicle.mileage)
#     print(my_vehicle)

#child class
#convertible class now inherits attributes from the vehicle class
class Convertible(Vehicle):
    def __init__(self,make,model,color,year,mileage,t_top=True):
        super().__init__(make,model,color,year,mileage)
        # self.make = make
        # self.model = model
        # self.color = color
        # self.year = year
        # self.mileage = mileage
        self.t_top = t_top

    # def honk(self):
    #     return "HOOOOOOOOOOOOOOOONK!"
    
    # def drive(self,miles_driven):
    #     self.mileage +=  miles_driven
    #     return self.mileage
    
    def change_top_status(self):
        if self.t_top:
            self.t_top = False
            return "T-top destroyed"
        else: 
            self.t_top = True
            return "Mullet Engaged"

    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles, mullet: {self.t_top}"
    
if __name__ == "__main__":
    my_vehicle = Convertible("Toyota","Camry","gray",2015,60000,t_top=False)

    print(my_vehicle.make)
    print(my_vehicle.mileage)
    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)
    print(my_vehicle)
    print(my_vehicle.t_top)
    print(my_vehicle.change_top_status())
    print(my_vehicle.t_top)
    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle)