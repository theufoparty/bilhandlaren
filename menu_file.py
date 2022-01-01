# Samling av hjälpfunktioner för menyerna i programmet.

def get_menu_option():
    try:
        option = int(input("Skriv in ditt val här: "))
    except:
        option = -1
    print("\n"*20)
    return option

def main_menu(title):
    print(title)
    print()
    print("[1] Är du kund?")
    print("[2] Är du företagare?")
    print("[0] Välj 0 för att avsluta programmet.")
    print()
    option = get_menu_option()
    print()
    return option

def customer_menu():
    print("Välkommen till kundmenyn, här kan du göra följande val: ")
    print()
    print("[1] Vill du sälja en bil?")
    print("[2] Vill du boka service/reparation?")
    print("[0] Välj 0 för att återgå till huvudmenyn.")
    print()
    option = get_menu_option()
    print()
    return option

def business_menu():
    print("Välkommen till företagsmenyn, här kan du göra följande val: ")
    print()
    print("[1] Vill du registera en bil?")
    print("[2] Vill du hantera personal?")
    print("[0] Välj 0 för att återgå till huvudmenyn.")
    print()
    option = get_menu_option()
    print()
    return option

def employee_menu():
    print("Vill du lägga till eller ta bort en anställd?")
    print()
    print("[1] Lägg till anställd")
    print("[2] Ta bort anställd")
    print("[0] Välj 0 för att återgå till företagasmenyn.")
    print()
    option = get_menu_option()
    print()
    return option