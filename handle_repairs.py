import car

def handle_repairs():
    print("Bokning av reparationsärende")
    print()
    print("Svara på dessa frågor angående din bil: ")
    brand = input("Vilket märke har din bil?: ")
    model = input("Vilken modell har bilen?: ")
    year = input("Vilken årsmodell har bilen?: ")
    try:
        mileage = int(input("Hur många km har bilen gått?: "))
    except:
        print("Ni måste ange antal km som siffror.")
    car_to_repair = car.Car(brand,model,year,mileage)
    date = input("Lämpligt datum: ")
    fault_to_repair = input("Vad har bilen för fel?: ")

    print("Du vill alltså boka in din bil:")
    car_to_repair.print()
    print("Med det här felet: "+ fault_to_repair +" på det här datumet: "+date+".")
    print()
    print("Vi återkommer inom kort!")
    print()
