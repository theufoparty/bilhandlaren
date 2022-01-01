import incorrect_option
import menu_file

employees = ["Johan", "David", "Klara", "Anna", "Nils"]

def print_employees():
  print("Här är en lista på all personal:")
  print()
  for name in employees:
    print("\t"+name)
  print()

def handle_employees():
  print("Välkommen till personalhantering!")
  print()
  print_employees()
  option = menu_file.employee_menu()
  while option != 0:
    if option == 1:
      name = input("Skriv in namn på ny anställd: ")
      print()
      employees.append(name)
    elif option == 2:
      name = input("Skriv in namn på anställd du vill ta bort: ")
      print()
      try: 
        employees.remove(name)
      except:
        print("Det ser ut som att "+name+" inte finns bland de anställda.")
    else:
        incorrect_option.incorrect_option()
    print_employees()
    option = menu_file.employee_menu()