import hämta_menyval

def företagare_meny():
    print("Välkommen till företagsmenyn, här kan du göra följande val: ")
    print()
    print("[1] Vill du registera en bil?")
    print("[2] Vill du hantera personal?")
    print("[0] Välj 0 för att avsluta programmet.")
    print()
    option = hämta_menyval.hämta_menyval()
    print()
    return option