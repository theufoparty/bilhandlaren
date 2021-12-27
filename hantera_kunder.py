import kund_meny
import repairs
import sell_car
import felaktigt_val

def hantera_kunder():
    option = kund_meny.kund_meny("Välkommen till kundmenyn, här kan du göra följande val: ")
    print()
    if option == 1:
        sell_car.sell_car()
    elif option == 2:
        repairs.repairs()
    else:
        felaktigt_val.felaktigt_val()