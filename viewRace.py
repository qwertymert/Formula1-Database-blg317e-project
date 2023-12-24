from flask import Blueprint, render_template, current_app, request
from MySqlRepository import MySQLRepository

viewRace = Blueprint('viewRace', __name__)

@viewRace.route("/races", methods=["GET", "POST"])
def races_page():
    repo = MySQLRepository()
    columns = repo.get_columns('races')

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        races_data = repo.read('races')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('races.html', races_data=races_data, columns=columns, table_names=table_names,bool=True)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('races.html', columns=columns, table_names=table_names,bool=False)
   
@viewRace.route("/races/filter_data", methods=["POST"])
def filter_data():
    repo = MySQLRepository()

    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')


    races_data = repo.read('races',filter, column)
    columns = repo.get_columns('races')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('races.html', races_data=races_data, columns=columns, table_names=table_names,bool=True)

@viewRace.route("/races/add_race", methods=["POST"])
def add_race():
    repo = MySQLRepository()
    

    # Getting all new data for all columns
    columns = repo.get_columns('races')[1:]
    data_to_add = {column: request.form.get(column) for column in columns}

    # Adding the new data to the teams table using repo method create
    repo.create('races', data_to_add)
    races_data = repo.read('races')
    columns = repo.get_columns('races')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('races.html', races_data=races_data, columns=columns, table_names=table_names,bool=False)

@viewRace.route("/races/update_race", methods=["POST"])
@viewRace.route("/races/update_race", methods=["POST"])
def update_race():
    repo = MySQLRepository()

    # Getting the race ID from the form data
    race_id = request.form.get('race_id')

    # Getting the updated data for all columns
    columns = repo.get_columns('races')[1:]
    data_to_update = {column: request.form.get(column) for column in columns}

    # Updating the race data using repo method update
    repo.update('races', race_id, data_to_update)

    races_data = repo.read('races')
    columns = repo.get_columns('races')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('races.html', races_data=races_data, columns=columns, table_names=table_names, bool=True)
    