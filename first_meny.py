# meny - första meny
def first_meny(title):
    print(title)
    print()
    print("[1] Är du kund?")
    print("[2] Är du företagare?")
    print("[0] Välj 0 för att avsluta programmet.")
    print()
    option = int(input("Skriv in ditt val här: "))
    print()
    return option