# Dies ist ein Programm das als Shopping Liste funktionieren soll
import sqlite3
from tkinter import *
from tkinter import ttk

# Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('shoppinglist.db')

# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = conn.cursor()

# Erstellung der Datenbank categories
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(32) NOT NULL
               )
''')

# Categories Datenbank befüllen
categorie_list = ["Gemüse", "Obst", "Backwaren", "Süßigkeiten", "Milchprodukte", "Getränke", "Fleisch & Fisch", "Belag", "Klamotten", "Technik", "Sonstiges"]
cursor.execute('''
            SELECT count(*) FROM categories
            ''')
empty = cursor.fetchone()
if empty[0] == 0:
    print("Categories Datatable wurde befüllt.")
    for i in categorie_list:
        cursor.execute('''
                INSERT INTO categories (name)
                VALUES (?)
            ''', (i,))
        conn.commit()

# Erstellung der Datenbank shoppinglist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shoppinglist(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               kategorie VARCHAR(32) NOT NULL,
               name VARCHAR(64) NOT NULL,
               amount INTEGER NOT NULL,
               price FLOAT NOT NULL,
               CONSTRAINT FK_KategorieCategorieName FOREIGN KEY(kategorie) REFERENCES categories(name)
               )
''')

def categories():
    cursor.execute('''
                SELECT * from categories
                   ''')
    categorie = cursor.fetchall()
    for i in categorie:
        categorie_list = print(i)
    return categorie_list

# Funktion um ein Item der Einkaufsliste hinzuzufügen
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll.\n")
    print("Welcher Kategorie soll der Artikelt hinzugefügt werden?")
    categories()
    while True:
        categorie_typ = input("Welcher Kategorie gehört der Artikel an? Bitte geben Sie die Nummer der Kategorie an.\n")
        categorie_typ_int = int(categorie_typ)
        if categorie_typ_int < 23:
            break
        else:
            print("Bitte gib die richtige Kategorie Nummer ein.")
    cursor.execute('SELECT * FROM categories WHERE id = ?', (categorie_typ))
    categorie = cursor.fetchone()
    categorie_name = categorie[1]
    amount = int(input(f"Wie oft möchten Sie {item} kaufen?\n"))
    price = float(input(f"Wie teuer ist {item}? Bitte mit mindestens einer Nachkomma Stelle angeben.\n"))
    if item:
        cursor.execute('''
            INSERT INTO shoppinglist (name, kategorie, amount, price)
            VALUES (?, ?, ?, ?)
        ''', (item, categorie_name, amount, price))
        conn.commit()
        print(f"Der Artikel {item} wurde {amount} mal der Einkaufsliste mit dem Preis {price}€ hinzugefügt. Der Artikel gehört der Kategorie {categorie_name} an.")
    else:
        print("Eingabe war leer und daher wird kein Artikelt hinzugefügt.")

# Funktion um die EInkaufsliste anzuzeigen
def show_shoppinglist():
    print("Deine Einkaufsliste:")
    cursor.execute('SELECT * FROM shoppinglist')
    shoppinglist = cursor.fetchall()
    if len(shoppinglist) != 0:
        for i in shoppinglist:
            print(f"Nummer: {i[0]}, Kategorie: {i[1]}, Artikel: {i[2]}, Anzahl: {i[3]}, Preis: {i[4]}")
    else:
        print("Deine Einkaufliste ist leer")

def update_shoppinglist():
    item_id = input("Welchen Artikel möchten Sie verändern? Bitte geben Sie die Nummer in der Einkauflist an.\n")
    cursor.execute('SELECT * FROM shoppinglist WHERE id = ?', (item_id))
    print("Sie können den")
    print("1. Namen")
    print("2. Kategorie")
    print("3. Menge")
    print("4. Preis")
    print("5. Alles ändern")
    print("verändern.")
    print("-----")
    choice = input("Was möchten Sie gerne verändern?\n")

    if choice == "1":
        item_name = input("Wie soll der Artikel nun heißen?\n")
        cursor.execute('''
            UPDATE shoppinglist SET name = ? WHERE id = ?
        ''', (item_name, item_id))
        conn.commit()
        print(f"Sie haben Erfolgreich den Artikel mit der Nummer {item_id} umbenannt in {item_name}.")
    
    elif choice == "2":
        while True:
            categories()
            categorie_typ = input("Welche Kategorie gehört der Artikel nun an?\n")
            categorie_typ_int = int(categorie_typ)
            if categorie_typ_int < 13:
                break
            else:
                print("Bitte gib die richtige Kategorie Nummer ein.")
        cursor.execute('SELECT * FROM categories WHERE id = ?', (categorie_typ))
        categorie = cursor.fetchone()
        print(categorie)
        categorie_name = categorie[1]
        cursor.execute('''
            UPDATE shoppinglist SET kategorie = ? WHERE id = ?
        ''', (categorie_name, item_id))
        conn.commit()
        print(f"Sie haben Erfolgreich die Kategorie vom Artikel mit der Nummer {item_id} geändert in {categorie_typ}.")

    elif choice == "3":
        item_amount = int(input("Wie viel wollen Sie nun kaufen?\n"))
        cursor.execute('''
            UPDATE shoppinglist SET amount = ? WHERE id = ?
            ''', (item_amount, item_id))
        conn.commit()
        print(f"Sie haben Erfolgreich die Menge vom Artikel mit der Nummer {item_id} geändert in {item_amount}.")
        
    elif choice == "4":
        item_price = float(input("Wie hoch ist der neue Preis?\n"))
        cursor.execute('''
            UPDATE shoppinglist SET price = ? WHERE id = ?
        ''', (item_price, item_id))
        conn.commit()
        print(f"Sie haben Erfolgreich den Preis vom Artikel mit der Nummer {item_id} geändert in {item_price}€.")

    elif choice == "5":
        item_name = input("Wie soll der Artikel nun heißen?\n")
        item_categorie = input("Wie soll die neue Kategorie lauten?\n")
        item_amount = int(input("Wie viel wollen Sie nun kaufen?\n"))
        item_price = float(input("Wie hoch ist der neue Preis?\n"))
        cursor.execute('''
            UPDATE shoppinglist SET name = ?, kategorie = ?, amount = ?, price = ? WHERE id = ?
        ''', (item_name, item_categorie, item_amount, item_price, item_id))
        conn.commit()

    else:
        print("Bitte wählen Sie nur zwischen 1, 2, 3 oder 4 aus.")

def delete_item_shoppinglist():
    item_name = input("Welchen Artikel möchten Sie von ihrer Einkaufsliste löschen? Bitte geben Sie den Namen an.\n")
    cursor.execute('''
    DELETE FROM students WHERE name = ?
    ''', (item_name)
    )
    conn.commit()
    print(f"Student mit der ID: {item_name} wurde entfernt.")

def search_shoppinglist():
    while True:
        choice = input("Möchten Sie nach der 1. Nummer, dem 2. Artikel, der 3. Kategorie, der 4. Anzahl oder dem 5. Preis suchen? Oder mit 6. die Suche beenden?\n")
        if choice == "1":
            item = input("Nach welcher Nummer wollen Sie suchen?\n")
            cursor.execute('SELECT * FROM shoppinglist WHERE id = ?', (item))
            itemlist = cursor.fetchall()
            for i in itemlist:
                print(f"Ihr gesuchtes Item ist: ID: {i[0]}, Kategorie: {i[1]} Artikel: {i[2]}, Anzahl: {i[3]}, Preis: {i[4]}")

        elif choice == "2":
            item_name = input("Nach welchem Artikel möchten Sie suchen?\n")
            item_syn_name = "%" + item_name + "%"
            cursor.execute("SELECT * FROM shoppinglist WHERE item LIKE ?", (item_syn_name,))
            itemlist = cursor.fetchall()
            for i in itemlist:
                print(f"Ihr gesuchtes Item ist: ID: {i[0]}, Kategorie: {i[1]} Artikel: {i[2]}, Anzahl: {i[3]}, Preis: {i[4]}")

        elif choice == "3":
            item_categorie = input("Nach welcher Kategorie wollen Sie suchen?\n")
            cursor.execute('SELECT * FROM shoppinglist WHERE kategorie = ?', (item_categorie))
            itemlist = cursor.fetchall()
            for i in itemlist:
                print(f"Ihr gesuchtes Item ist: ID: {i[0]}, Kategorie: {i[1]} Artikel: {i[2]}, Anzahl: {i[3]}, Preis: {i[4]}")

        elif choice == "4":
            item_amount = int(input("Nach welcher Anzahl möchten Sie suchen?\n"))
            cursor.execute('SELECT * FROM shoppinglist WHERE amount = ?', (item_amount,))
            itemlist = cursor.fetchall()
            for i in itemlist:
                print(f"Ihr gesuchtes Item ist: ID: {i[0]}, Kategorie: {i[1]} Artikel: {i[2]}, Anzahl: {i[3]}, Preis: {i[4]}")

        elif choice == "5":
            item_price = float(input("Nach welchem Preis möchten Sie suchen?\n"))
            cursor.execute('SELECT * FROM shoppinglist WHERE price = ?', (item_price,))
            itemlist = cursor.fetchall()
            for i in itemlist:
                print(f"Ihr gesuchtes Item ist: ID: {i[0]}, Kategorie: {i[1]} Artikel: {i[2]}, Anzahl: {i[3]}, Preis: {i[4]}")
        
        elif choice == "6":
            print("Die Suche wird beendet.")
            break

        else:
            print("Bitte geben Sie nur 1, 2, 3, 4, 5 oder 6 an.")

# Main Function
def main():
    while True:
        print("\n----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Nach einem bestimmten Artikel in der Einkaufsliste suchen")
        print("4. Einen Artikel aktualisieren")
        print("5. Einen Artikel von der Einkaufsliste löschen")
        print("6. Programm beenden")
        print("-----")
        choice = input("Bitte wähle aus was du machen möchtest: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            show_shoppinglist()
        
        elif choice == "3":
            search_shoppinglist()

        elif choice == "4":
            update_shoppinglist()

        elif choice == "5":
            delete_item_shoppinglist()

        elif choice == "6":
            print("Programm wird beendet! Tschüssi.")
            break

        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2, 3, 4, 5 oder 6")

if __name__ == "__main__":
    main()
    # dickus = "Hello World!"
    # root = Tk()
    # frm = ttk.Frame(root, padding = 10)
    # frm.grid()
    # ttk.Label(frm, text = dickus).grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
    # root.mainloop()