# shoppinglist.py

# Leere Einkaufsliste
shoppinglist = []

# Funktion zum Hinzufügen eines Artikels
def add_item():
    item = input("Welche Artikel sollen auf die Einkaufsliste hinzugefügt werden: ")
    shoppinglist.append(item)
    print(f"{item} wurde der Einkaufsliste hinzugefügt.")

# Einkaufsliste mit Arikeln
if __name__ == "__main__":
    add_item()
    print("Aktuelle Einkaufsliste:", shoppinglist)
