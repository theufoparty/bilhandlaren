import car
import menu_file
import incorrect_option

# Funktion för att kunder ska kunna boka reparationer. 

def handle_repairs():
    option = 1
    while option != 0:
        if option == 1:
            print("Bokning av reparationsärende")
            print()
            print("Svara på dessa frågor angående din bil: ")
            print()
            car_to_repair = car.input_car()
            date = input("Lämpligt datum: ")
            fault_to_repair = input("Vad har bilen för fel?: ")
            print()
            print("Du vill alltså boka in din bil: ")
            car_to_repair.print()
            print("Med det här felet: " + fault_to_repair + " på det här datumet: " + date + ".")
            print()
            print("Vi återkommer inom kort!")
            print()
        else:
            incorrect_option.incorrect_option()
        option = menu_file.confirm_menu("Vill du boka en till tid?")
