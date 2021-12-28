import felaktigt_val
import meny_file

anställda = ["Johan", "David", "Klara", "Anna", "Nils"]

def print_anställda():
  print("Här är en lista på all personal:")
  print()
  print(anställda)
  print()

def personal():
  print("Välkommen till personalhantering!")
  print()
  option = meny_file.personal_meny()
  while option != 0:
    if option == 1:
      namn = input("Skriv in namn på ny anställd: ")
      print()
      anställda.append(namn)
    elif option == 2:
      namn = input("Skriv in namn på anställd du vill ta bort: ")
      print()
      try: 
        anställda.remove(namn)
      except:
        print("Det ser ut som att "+namn+" inte finnsbland the anställda.")
    else:
        felaktigt_val.felaktigt_val()
    print_anställda()
    option = meny_file.personal_meny()