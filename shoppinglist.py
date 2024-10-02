# shoppinglist.py

# Leere Einkaufsliste
shoppinglist = []

# Funktion zum Hinzufügen eines Artikels
def add_item():
    item = input("Welche Artikel sollen auf die Einkaufsliste hinzugefügt werden: ")
    shoppinglist.append(item)
    print(f"{item} wurde der Einkaufsliste hinzugefügt.")

# Anzeigen der Einkaufsliste
def show_shoppinglist():
    if shoppinglist == []:
        print("Noch keine Artikel hinzugefügt.")
    else:
        for item in shoppinglist:
            print(item)

# Einkaufsliste mit Arikeln
if __name__ == "__main__":
    show_shoppinglist()