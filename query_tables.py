import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="" # Change with your root password
)

mycursor = mydb.cursor()

mycursor.execute("use PUBLICATIONS")

print("-"*15, "Show PUBLISHER table", "-"*15)
mycursor.execute("select * from PUBLISHER;")
for x in mycursor:
    print(x)

print("-"*15, "Show AUTHOR table", "-"*15)
mycursor.execute("select * from author;")
for x in mycursor:
    print(x)
    
print("-"*15, "Show BOOK table", "-"*15)
mycursor.execute("select * from book;")
for x in mycursor:
    print(x)
    
mycursor.close()
mydb.close()
mycursor.close()