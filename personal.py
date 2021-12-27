import local_meny
import felaktigt_val
def personal():
    option = local_meny.local_meny("Vill du hantera personal?")
    while option != 2:
        if option == 1:
          print("Här finns en lista över all personal: ")
        else:
            felaktigt_val.felaktigt_val()
        option = local_meny.local_meny("Vill du hantera mer personalfrågor?")