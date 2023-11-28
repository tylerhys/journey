import sqlite3

# Create DB
db = sqlite3.connect("C:\\Users\\Tyler\\Documents\\GitHub\\journey\\01-Programming-Language\\01-Python\\01-100-Days-of-Code\\63-Virtual-Library\\practice1\\books-collection.db")
cursor = db.cursor()

#Create Table
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Insert Data into table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()