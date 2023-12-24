from flask import Blueprint, render_template, current_app, request
from MySqlRepository import MySQLRepository

viewTeam = Blueprint('viewTeam', __name__)  

@viewTeam.route("/teams", methods=["GET", "POST"])
def teams_page():
    repo = MySQLRepository()

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        teams_data = repo.read('constructors')
        columns = repo.get_columns('constructors')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('teams.html', table_names=table_names)


@viewTeam.route("/teams/add_team", methods=["POST"])
def add_team():
    repo = MySQLRepository()

    # Getting all new data for all columns
    columns = repo.get_columns('constructors')[1:]
    data_to_add = {column: request.form.get(column) for column in columns}

    # Adding the new data to the teams table using repo method create
    repo.create('constructors', data_to_add)
    teams_data = repo.read('constructors')
    columns = repo.get_columns('constructors')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names)