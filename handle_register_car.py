import car

def handle_register_car():

  print("Registrera följande uppgifter rörande bilen i databasen: ")
  print()
  brand = input("Vilket märke har bilen?: ")
  model = input("Vilken modell har bilen?: ")
  year = input("Vilken årsmodell har bilen?: ")
  try:
    mileage = int(input("Hur många km har bilen gått?: "))
  except:
    print("Ni måste ange antal km som siffror.")
  car_to_register = car.Car(brand,model,year,mileage)
  print()
  print("Följande bil finns nu registerad i systemet: ")
  print()
  car_to_register.print()
  print()