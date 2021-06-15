from .database_connection import Databaseconnection

books_file = 'books.json'


def creat_book_table():
    with Databaseconnection('data.db') as connection:
        Cursor = connection.cursor()
        Cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    



def add_book(name, author):
    with Databaseconnection('data.db') as connection:
        Cursor = connection.cursor()
        Cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name , author,))

    



def get_all_books():
    with Databaseconnection('data.db') as connection:
        Cursor = connection.cursor()
        Cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in Cursor.fetchall()]
        
    return books



def mark_book_as_read(name):
    with Databaseconnection('data.db') as connection:
        Cursor = connection.cursor()
        Cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

        
    
 

def delete_book(name):
    with Databaseconnection('data.db') as connection:
        Cursor = connection.cursor()
        Cursor.execute('DELETE FROM books WHERE name=?', (name,))


