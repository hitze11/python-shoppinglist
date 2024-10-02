# shoppinglist.py

# Leere Einkaufsliste
shoppinglist = []

#  Hinzufügen eines Artikels
def add_item():
    item = input("Welche Artikel sollen dem Einkaufszettel hinzugefügt werden?: ")
    shoppinglist.append(item)
    print(f"{item} wurde dem Eikaufszettel hinzugefügt.")

# Anzeigen der Einkaufsliste
def show_shoppinglist():
    if shoppinglist:
        print("Einkaufszettel:")
        for item in shoppinglist:
            print(f"- {item}")  
    else:
        print("Dein Einkaufszettel ist leer.")

# Hauptfunktion, um das Programm zu steuern
def main():
    while True:
        print("\n----- Einkaufszettel -----")
        print("1. Artikel zum Einkaufszettel hinzufügen")
        print("2. Einkaufszettel anzeigen")
        print("3. Programm beenden")
        
        # Benutzerauswahl
        choice = input("Bitte wähle eine Option (1, 2 oder 3): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen.")
            break  
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")

# Einkaufszettel anzeigen
if __name__ == "__main__":
    main()
