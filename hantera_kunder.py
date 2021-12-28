import meny_file
import repairs
import sell_car
import felaktigt_val

def hantera_kunder():
    option = meny_file.kund_meny()
    if option == 1:
        sell_car.sell_car()
    elif option == 2:
        repairs.repairs()
    else:
        felaktigt_val.felaktigt_val()