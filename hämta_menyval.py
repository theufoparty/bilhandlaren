def hämta_menyval():
    try:
        option = int(input("Skriv in ditt val här: "))
    except:
        option = -1
    return option