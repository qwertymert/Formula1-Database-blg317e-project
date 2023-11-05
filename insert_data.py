import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="" # Change with your root password
)
mycursor = mydb.cursor()

mycursor.execute("use PUBLICATIONS")

# Insert data into PUBLISHER table
mycursor.execute("insert into PUBLISHER values (10, 'Addison-Wesley', '212-303-8421');")
mycursor.execute("insert into PUBLISHER values (20, 'Pearson Prentice Hall', '212-303-8423');")
mycursor.execute("insert into PUBLISHER values (30, 'McGraw-Hill', '216-404-02354');")
print("Publications inserted")



# Insert data into AUTHOR table with a example function
def insert_into_publisher_table(publisher_id, publisher_name, publisher_email):
    mycursor.execute("""
                    insert into author values ({}, '{}', '{}');
                    """.format(publisher_id, publisher_name, publisher_email))

insert_into_publisher_table(100, 'Elmasri', 'elm@uta')
insert_into_publisher_table(200, 'Ullman', 'ulm@ibm')
insert_into_publisher_table(300, 'Weinberg', None)
insert_into_publisher_table(400, 'Silberschatz', 'slb@ms')
insert_into_publisher_table(500, 'Ramakrishnan', 'rma@wisc')
print("Authors inserted")



# Insert data into BOOK table with a example function
def insert_into_book_table(ISBN, publisher_id, author_id, title):
    mycursor.execute("""
                    insert into book values ('{}', {}, '{}', '{}');
                    """.format(ISBN, publisher_id, author_id, title))
    
insert_into_book_table('A0012345', 10, 100, 'Fundamentals of Database Systems')
insert_into_book_table('B0033224', 20, 200, 'Database Systems The Complete Book')
insert_into_book_table('C0092831', 30, 300, 'SQL The Complete Reference')
insert_into_book_table('D0027354', 30, 400, 'Database System Concepts')
insert_into_book_table('E0091237', 30, 500, 'Database Management Systems')
insert_into_book_table('F0072261', 20, 100, 'Database Design')
print("Books inserted")

mydb.commit()

mycursor.close()
mydb.close()
