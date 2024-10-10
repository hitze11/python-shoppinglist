# Dies ist ein Programm das als Shopping Liste funktionieren soll
 
# Erstellung der Liste
shoppinglist = []

# Funktion um ein Item der Liste hinzuzufügen
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    if item:
        shoppinglist.append(item)
        print(f"Der Artikel {item} wurde der Einkaufsliste hinzugefügt")
    else:
        print("Eingabe war leer und daher wird kein Artikelt hinzugefügt.")

# Aufruf der Funktion add_item
# add_item(input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: "))

# Funktion um die EInkaufsliste anzuzeigen
def show_shoppinglist():
    print("Deine Einkaufsliste:")
    if len(shoppinglist) != 0:
        for i in (shoppinglist):
            print(i)
    else:
        print("Deine Einkaufliste ist leer")

# Aufruf der Funktion show_shoppinglist
# show_shoppinglist()

# Main Function
def main():
    while 1 == 1:
        print("\n----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        choice = input("Bitte wähle aus was du machen möchtest: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen.")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")

if __name__ == "__main__":
    main()