import os

scripts_path = "csv_to_database"

tables = ["drivers", "circuits", "races", "driverStandings",
          "pitStops", "lapTimes", "constructors", "constructorStandings",
          "constructorResults", "qualifying", "results", "status", "seasons"]

# Creates database and tables if they don't exist
os.system(f"python create_tables.py")

# Fills tables with data if they are empty
for table in tables:
    os.system(f"python {scripts_path}/crud_{table}.py")