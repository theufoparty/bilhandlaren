def kund_meny():
    print("Välkommen till kundmenyn, här kan du göra följande val: ")
    print()
    print("[1] Vill du sälja en bil?")
    print("[2] Vill du boka service/reparation?")
    print("[0] Välj 0 för att avsluta programmet.")
    print()
    option = int(input("Skriv in ditt val här: "))
    print()
    return option