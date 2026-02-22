class Car:
    
    # init method (Constructor in Java) to store all attributes Year Make Model
    def __init__(self,year,make,model):
        self.year=year
        self.make=make
        self.model=model

    # print Year Make Model in one line
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


my_car = Car(2020,"Toyota","Corolla")
my_car.describe_car()