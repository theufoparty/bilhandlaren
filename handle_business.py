import menu_file
import handle_employees
import handle_register_car
import incorrect_option

# Menyfunktion för att hantera företagsval i programmet.

def handle_business():
    option = menu_file.business_menu()
    while option != 0:
        if option == 1:
            handle_register_car.handle_register_car()
        elif option == 2:
            handle_employees.handle_employees()
        else:
            incorrect_option.incorrect_option()
        option = menu_file.business_menu()