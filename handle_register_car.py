import car
import menu_file
import incorrect_option

# Funktion för att företaget ska kunna registera bilar.

def handle_register_car():
	option = 1
	while option != 0:
		if option == 1:	
			print("Registrera följande uppgifter rörande bilen i databasen: ")
			print()
			car_to_register = car.input_car()
			print()
			print("Följande bil finns nu registerad i systemet: ")
			print()
			car_to_register.print()
			print()
		else:
			incorrect_option.incorrect_option()
		option = menu_file.confirm_menu("Vill du registrera en till bil?")