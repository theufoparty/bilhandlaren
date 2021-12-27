import hämta_menyval

def local_meny(titel):
    print(titel)
    print()
    print("[1] Ja")
    print("[2] Nej") 
    print()
    option = hämta_menyval.hämta_menyval()
    print()
    return option
