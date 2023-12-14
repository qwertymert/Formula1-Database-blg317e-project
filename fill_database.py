import os

scripts_path = "csv_to_database"

tables = ["drivers", "circuits", "races", "driverStandings",
          "pitStops", "lapTimes", "constructors", "constructorStandings",
          "constructorResults", "qualifying", "results", "status", "seasons"]

for table in tables:
    os.system(f"python {scripts_path}/crud_{table}.py")