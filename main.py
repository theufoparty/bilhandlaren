# Bilhandlaren - en interaktiv terminalmeny för bilhandel i andrahand.

import first_meny
import felaktigt_val
import hantera_företagare
import hantera_kunder

print()
option = first_meny.first_meny("Välkommen till Nell's Bilhandel!")

while option != 0:
    if option == 1: 
        hantera_kunder.hantera_kunder()
    elif option == 2:
        hantera_företagare.hantera_företagare()
    else: 
        felaktigt_val.felaktigt_val() 
    option = first_meny.first_meny("Välkommen till Nell's Bilhandel!")

print("Tack för att du använt programmet, välkommen åter!")