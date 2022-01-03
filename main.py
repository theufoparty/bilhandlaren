import menu_file
import handle_customer
import handle_business
import incorrect_option

# Bilhandlaren - en interaktiv terminalmeny för bilhandel i andrahand

print() 

option = menu_file.main_menu("Välkommen till Nell's Bilhandel!")

while option != 0:
    if option == 1: 
        handle_customer.handle_customer()
    elif option == 2:
        handle_business.handle_business()
    else: 
        incorrect_option.incorrect_option() 
    option = menu_file.main_menu("Välkommen till Nell's Bilhandel!")

print("Tack för att du använt programmet, välkommen åter!")