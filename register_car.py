import meny_file
import felaktigt_val

def register_car():
    option = meny_file.local_meny("Vill du registrera en bil?")
    while option != 2:
        if option == 1:
          print("Skriv in följande information rörande bilen nedan: ")
          print()
          bilmärke_1 = input("Vilket bilmärke har bilen? ")
          bilmodell_1 = input("Vilken modell är bilen? ")
          årsmodell_1 = input("Vilken årsmodell är bilen? ")
          körsträcka_1 = input("Hur långt har bilen gått? ")
          print()
          print("Tack för uppgifterna, nu finns följande registrerat: ")
          print()
          print(bilmärke_1)
          print(bilmodell_1)
          print(årsmodell_1)
          print(körsträcka_1)
        else:
            felaktigt_val.felaktigt_val()
        option = meny_file.local_meny("Vill du registrera en till bil?")