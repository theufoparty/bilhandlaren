import car

def handle_sell_car():
    print("Svara på dessa frågor angående din bil: ")
    print()
    car_to_sell = car.input_car()
    print()
    print("Du har alltså följande bil:")
    print()
    car_to_sell.print()
    print()
    print('vi estimerar bilens värde till ' + str(car_to_sell.worth()) + ". Detta låter intressant, vi återkommer inom kort.")
    print()