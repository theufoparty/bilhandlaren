import menu_file
import handle_repairs
import handle_sell_car
import incorrect_option

# Menyfunktion för att hantera kundval i programmet.

def handle_customer():
    option = menu_file.customer_menu()
    while option != 0:
        if option == 1:
            handle_sell_car.handle_sell_car()
        elif option == 2:
            handle_repairs.handle_repairs()
        else:
            incorrect_option.incorrect_option()
        option = menu_file.customer_menu()