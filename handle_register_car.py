import car

# Funktion för att företaget ska kunna registera bilar.

def handle_register_car():
  print("Registrera följande uppgifter rörande bilen i databasen: ")
  print()
  car_to_register = car.input_car()
  print()
  print("Följande bil finns nu registerad i systemet: ")
  print()
  car_to_register.print()
  print()