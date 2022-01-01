import car

def handle_sell_car():
    print("Svara på dessa frågor angående din bil: ")
    print()
    brand = input("Vilket märke har din bil?: ")
    model = input("Vilken modell har bilen?: ")
    year = input("Vilken årsmodell har bilen?: ")
    try:
        mileage = int(input("Hur många km har bilen gått?: "))
    except:
        print("Ni måste ange antal km som siffror.")
    car_to_sell = car.Car(brand,model,year,mileage)
    print()
    print('Du har alltså en bil av märket '+brand+ ' av '+model+'-modell, från '+year+' som har gått '+str(mileage)+' km, vi estimerar bilens värde till ' + str(car_to_sell.worth()) + ". Detta låter intressant, vi återkommer inom kort.")
    print()