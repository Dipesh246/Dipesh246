from utils import database

USER_CHOICE = """
Enter:
-'a'to add a new books
-'l' to list all books
-'r' to read books
-'d' to delete a books
-'q' to quit


Your choice: """

def menu():
    database.creat_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q' :
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_books()
        elif user_input == 'd':
            prompt_delete_books()
        else:
            print("Unkown command. Please try again.")

        user_input = input(USER_CHOICE)    

def prompt_add_book():
    name = input('Enter new Book name: ')
    author = input('Enter new Books Author name: ')

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")
        


def prompt_read_books():
    name = input ('Enter the name of book You judt finished reading:  ')
    database.mark_book_as_read(name)



def prompt_delete_books():
    name = input('Enter the name of the book you widh to delete:')

    database.delete_book(name)

menu()     