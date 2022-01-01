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