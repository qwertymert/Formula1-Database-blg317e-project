import mysql.connector
import yaml

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

del db_config['database']

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()

with open('schema.sql', encoding="utf-8") as f:
    str1 = f.read()
    sql_commands = str1.split(';')
    sql_commands = [x.strip() for x in sql_commands]
    sql_commands = list(filter(lambda x: x != '', sql_commands))
    for i in range(len(sql_commands)):
        mycursor.execute(sql_commands[i])

mydb.commit()

mycursor.close()
mydb.close()