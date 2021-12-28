import meny_file
import felaktigt_val

def sell_car():
    option = meny_file.local_meny("Vill du sälja en bil till oss?")
    while option != 2:
        if option == 1:
            print("Svara på dessa frågor angående din bil: ")
            print()
            bilmärke = input("Vilket märke har din bil?: ")
            modellbeteckning = input("Vilken modell har bilen?: ")
            årsmodell = input("Vilken årsmodell har bilen?: ")
            antal_km = input("Hur många km har bilen gått?: ")
            print()
            print('Du har alltså en bil av märket '+bilmärke+' av '+modellbeteckning+'-modell, från '+årsmodell+' som har gått '+antal_km+' km, detta låter intressant, vi återkommer inom kort.')
        else:
            felaktigt_val.felaktigt_val()
        option = meny_file.local_meny("Vill du sälja en till bil?")