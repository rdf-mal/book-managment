# Bookmanagement
import repo_csv as repo
import tui
import management


# Hauptprogramm
def main():
    # Load book data from CSV file
    file = "bestand.csv"

    try:
        all_books = repo.load_books(file)
    except FileNotFoundError:
        tui.display_error(f"Datei '{file}' nicht gefunden.")
        tui.display_info("Programm wird beendet.")
        return # exit if file does not exist
   
    while True:
        tui.display_menu()
        user_choice = tui.get_user_choice()
        tui.clear_screen()
        # using a match here instead multiple if - elif bloocks 
        match user_choice:
            case 1: # Alle Bücher anzeigen
                tui.display_list_of_books(all_books)
            case 2: # Verfügbare Bücher anzeigen
                available_books = management.filter_for_available_books(all_books)
                tui.display_list_of_books(available_books)
            case 3: # Ausgeliehene Bücher anzeigen
                borrowed_books = management.filter_for_borrowed_books(all_books)
                tui.display_list_of_books(borrowed_books)
            case 4: # Buch hinzufügen
                new_book = tui.get_book_details_from_user()
                all_books.append(new_book)
                tui.display_info(f"Buch {new_book["title"]} hinzugefügt.")
                repo.save_books(file, all_books)
            case 5: # Buch löschen
                # User Namen des Buchs eingeben lassen:
                book_name = tui.get_book_name_from_user()
                if management.remove_book(book_name, all_books):
                    tui.display_info(f"Buch {book_name} gelöscht.")
                    repo.save_books(file, all_books)
                else:
                    tui.display_info(f"Buch {book_name} nicht gefunden.")
            case 6: # Buch ausleihen
                tui.display_list_of_books(all_books)
                isbn = tui.get_isbn_from_user()
                for book in all_books:
                    if book["isbn"] == isbn:
                        if management.borrow_book(book):
                            tui.display_info(f"Buch {book["title"]} ausgeliehen")
                        else:
                            tui.display_error(f"Buch {book["title"]} nicht mehr verfügbar.")
                        break

            case 7: # Buch zurückgeben
                pass # TODO implement this
            case 0: # exit the programm
                repo.save_books(file, all_books)
                tui.display_info("Programm wird beendet.")
                return
        # Pause before showing the menu again    
        tui.wait_for_user_interaction()


if __name__ == "__main__":
    main()
