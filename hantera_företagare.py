import personal
import felaktigt_val
import register_car
import meny_file

def hantera_företagare():
    option = meny_file.företagare_meny()
    if option == 1:
        register_car.register_car()
    elif option == 2:
        personal.personal()
    else:
        felaktigt_val.felaktigt_val()