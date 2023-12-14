import mysql.connector
import pandas as pd
import yaml

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_constructor = pd.read_csv('data/constructors.csv', encoding='ISO-8859-1')

def insert_constructors(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into constructors values (%s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))

try:
    for i, record in df_constructor.iterrows():
        insert_constructors(record)
    print("Constructors inserted")
except mysql.connector.errors.IntegrityError as err:
    print("Constructors already inserted")
except Exception as err:
    print(err)

mydb.commit()

mycursor.close()
mydb.close()
