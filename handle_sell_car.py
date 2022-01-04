import car
import menu_file
import incorrect_option

# Funktion för att kunder ska kunna sälja bilar till bilhandeln.

def handle_sell_car():
    option = 1
    while option != 0:
        if option == 1:
            print("Svara på dessa frågor angående din bil: ")
            print()
            car_to_sell = car.input_car()
            print()
            print("Du har alltså följande bil:")
            print()
            car_to_sell.print()
            print()
            print('Vi estimerar bilens värde till ' + str(car_to_sell.worth()) + ". Detta låter intressant, vi återkommer inom kort.")
            print()
        else:
            incorrect_option.incorrect_option()
        option = menu_file.confirm_menu("Vill du sälja en till bil?")