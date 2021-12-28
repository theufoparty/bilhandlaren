import meny_file
import felaktigt_val

def repairs():
    option = meny_file.local_meny("Vill du boka reperationer av din bil?")
    while option != 2:
        if option == 1:
            print("Frågor om reperationsbokning")
            print()
            datum = input("Lämpligt datum: ")
            felmeddelande = input("Fel på bilen: ")
            print()
            print('Du vill alltså boka in din bil den '+datum+' på grund av det här felet på bilen: '+felmeddelande+'.')
        else:
            felaktigt_val.felaktigt_val()
        option = meny_file.local_meny("Vill du boka en till tid?")