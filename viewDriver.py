from flask import Blueprint, render_template, current_app, request
from MySqlRepository import MySQLRepository

viewDriver = Blueprint('viewDriver', __name__)

@viewDriver.route("/drivers", methods=["GET", "POST"])
def drivers_page():
    repo = MySQLRepository()  # Assuming current_app is available
    columns = repo.get_columns('drivers')

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        drivers_data = repo.read('drivers')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('drivers.html', drivers_data=drivers_data, columns=columns, table_names=table_names,bool=True)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('drivers.html', columns=columns, table_names=table_names,bool=False)

@viewDriver.route("/drivers/filter_data", methods=["POST"])
def filter_data():
    repo = MySQLRepository()

    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')


    drivers_data = repo.read('drivers',filter, column)
    columns = repo.get_columns('drivers')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('drivers.html', drivers_data=drivers_data, columns=columns, table_names=table_names,bool=True)