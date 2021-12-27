import företagare_meny
import personal
import felaktigt_val
import register_car

def hantera_företagare():
    option = företagare_meny.företagare_meny()
    print()
    if option == 1:
        register_car.register_car()
    elif option == 2:
        personal.personal()
    else:
        felaktigt_val.felaktigt_val()