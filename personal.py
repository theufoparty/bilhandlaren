import meny_file
import felaktigt_val

def personal():
    option = meny_file.local_meny("Vill du hantera personal?")
    while option != 2:
        if option == 1:
          print("Här finns en lista över all personal: ")
        else:
            felaktigt_val.felaktigt_val()
        print()
        option = meny_file.local_meny("Vill du hantera mer personalfrågor?")