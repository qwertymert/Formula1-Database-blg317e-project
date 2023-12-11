import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_status = pd.read_csv('data/status.csv', encoding='ISO-8859-1')

print(df_status.columns)

def insert_status(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    # if record[-3] is not None:
    #     record[-3] = pd.to_datetime(record[-3]).strftime('%Y-%m-%d')
    insert_sql = "insert into status values (%s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    


for i, record in df_status.iterrows():
    insert_status(record)
print("Races inserted")


mydb.commit()

mycursor.close()
mydb.close()
