from flask import Blueprint, render_template, current_app, request
from MySqlRepository import MySQLRepository

viewDriver = Blueprint('viewDriver', __name__)

@viewDriver.route("/drivers", methods=["GET", "POST"])
def drivers_page():
    repo = MySQLRepository()  # Assuming current_app is available

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        drivers_data = repo.read('drivers')
        columns = repo.get_columns('drivers')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('drivers.html', drivers_data=drivers_data, columns=columns, table_names=table_names)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('drivers.html', table_names=table_names)
