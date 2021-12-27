# local_meny - för mindre sub-val inuti menyn 
def local_meny(titel):
    print(titel)
    print()
    print("[1] Ja")
    print("[2] Nej") 
    print()
    option = int(input("Skriv in ditt val här: "))
    return option