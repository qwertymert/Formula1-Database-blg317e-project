import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="" # Change with your root password
)

mycursor = mydb.cursor()

print("-"*15, "Databases", "-"*15)
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)


# Create PUBLICATIONS database if not exists
mycursor.execute("CREATE DATABASE IF NOT EXISTS PUBLICATIONS")
mycursor.execute("use PUBLICATIONS")

print("-"*15, "Databases after creating publications", "-"*15)
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
    
mycursor.execute('''
                    create table if not exists publisher 
                        (publisher_id int,
                        publisher_name varchar(50),
                        phone char(15),
                        primary key (publisher_id)
                        );
                 '''
                 )

mycursor.execute('''
                    create table if not exists author 
                        (author_id int,
                        author_name varchar(20),
                        email varchar(20),
                        primary key (author_id)
                        );
                 '''
                )

mycursor.execute('''
                    create table if not exists book
                        (ISBN char(20),
                        publisher_id int,
                        author_id int,
                        title varchar(50),
                        primary key (ISBN, publisher_id, author_id),
                        foreign key (publisher_id) references publisher (publisher_id),
                        foreign key (author_id) references author (author_id)
                        );
                 '''
                 )

print("-"*15, "Show and describe tables", "-"*15)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
print()
mycursor.execute("DESCRIBE publisher")
for x in mycursor:
    print(x)
print()

mycursor.execute("DESCRIBE author")
for x in mycursor:
    print(x)
print()

mycursor.execute("DESCRIBE book")
for x in mycursor:
    print(x)
print()