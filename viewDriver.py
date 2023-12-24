from flask import Blueprint, render_template, current_app, request,redirect,url_for, jsonify
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


@viewDriver.route("/drivers/add_driver", methods=["POST"])
def add_driver():
    repo = MySQLRepository()

    # Getting all new data for all columns except driver_id since it is primary, will be filled auto.
    columns = repo.get_columns('drivers')[1:]
    data_to_add = {column: request.form.get(column) for column in columns}

    # Adding the new data to the drivers table using repo method create
    repo.create('drivers', data_to_add)
    drivers_data = repo.read('drivers')
    columns = repo.get_columns('drivers')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('drivers.html', drivers_data=drivers_data, columns=columns, table_names=table_names,bool=False)


@viewDriver.route("/drivers/update_driver", methods=["POST"])
def update_driver():
    repo = MySQLRepository()
    columns = repo.get_columns('drivers')
    form_data = request.form.to_dict()
    print(form_data)
    driver_id = form_data.pop  ('driverId', None)
    if driver_id is not None:
            condition = {"driverId": driver_id}
            repo.update('drivers', form_data, condition)
            
    drivers_data = repo.read('drivers')    
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    
    return render_template('drivers.html', drivers_data=drivers_data, columns=columns, table_names=table_names,bool=True)


    


@viewDriver.route("/drivers/delete_driver/<int:driver_id>", methods=["GET"])
def delete_driver(driver_id):
    repo = MySQLRepository()

    # Adding the new data to the drivers table using repo method delete
    repo.delete('drivers', driver_id, 'driverId')
    
    # Redirect to the drivers page after deleting
    return redirect(url_for('viewDriver.drivers_page'))
