


def print_menu():
    print("""
        --------------MENU-------------
        1. Pridanie noveho cisla
        2. Odstrániť číslo (Všetky výskyty)
        3. Zobraziť obsah zoznamu
        4. Kontrola hodnoty
    """)

print_menu()


def pridanie_cisla():
    volba = int(input("Zadaj cislo"))

    if volba == 1:
        try:
            number = int(input("Zadaj cislo ktore chces pridat:"))
        except ValueError:
            print("Nezadal si cislo")
    else:
        ll.append(number)
        print("\n Tvoj linked list je:")


