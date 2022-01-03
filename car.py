# Klass för bil.

class Car:
    brand = ""
    model = ""
    year = ""
    mileage = 0

    def __init__(self,brand,model,year,mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def worth(self):
        return 2000000 - self.mileage

    def print(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.mileage)

def input_car():
    brand = input("Vilket märke har bilen?: ")
    model = input("Vilken modell har bilen?: ")
    year = input("Vilken årsmodell har bilen?: ")
    try:
        mileage = int(input("Hur många km har bilen gått?: "))
    except:
        print("Ni måste ange antal km som siffror.")
    return Car(brand,model,year,mileage)