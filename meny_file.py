
def hämta_menyval():
    try:
        option = int(input("Skriv in ditt val här: "))
    except:
        option = -1
    print("\n"*20)
    return option

def first_meny(title):
    print(title)
    print()
    print("[1] Är du kund?")
    print("[2] Är du företagare?")
    print("[0] Välj 0 för att avsluta programmet.")
    print()
    option = hämta_menyval()
    print()
    return option

def local_meny(titel):
    print(titel)
    print()
    print("[1] Ja")
    print("[2] Nej") 
    print()
    option = hämta_menyval()
    print()
    return option

def kund_meny():
    print("Välkommen till kundmenyn, här kan du göra följande val: ")
    print()
    print("[1] Vill du sälja en bil?")
    print("[2] Vill du boka service/reparation?")
    print("[0] Välj 0 för att avsluta programmet.")
    print()
    option = hämta_menyval()
    print()
    return option

def företagare_meny():
    print("Välkommen till företagsmenyn, här kan du göra följande val: ")
    print()
    print("[1] Vill du registera en bil?")
    print("[2] Vill du hantera personal?")
    print("[0] Välj 0 för att avsluta programmet.")
    print()
    option = hämta_menyval()
    print()
    return option

def personal_meny():
    print("Vill du lägga till eller ta bort en anställd?")
    print()
    print("[1] Lägg till anställd")
    print("[2] Ta bort anställd")
    print()
    option = hämta_menyval()
    print()
    return option