from flask import Blueprint, render_template, current_app, request,redirect,url_for, url_for
from MySqlRepository import MySQLRepository

viewTeam = Blueprint('viewTeam', __name__)  

@viewTeam.route("/teams", methods=["GET", "POST"])
def teams_page():
    repo = MySQLRepository()
    columns = repo.get_columns('constructors')

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all teams
        teams_data = repo.read('constructors')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names,bool=True)
    else:
        # Otherwise, fetch a limited number of teams (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('teams.html', columns=columns, table_names=table_names,bool=False)

@viewTeam.route("/teams/filter_data", methods=["POST"])
def filter_data():
    repo = MySQLRepository()

    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')


    teams_data = repo.read('constructors',filter, column)
    columns = repo.get_columns('constructors')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names,bool=True)

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
    return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names,bool=False)

@viewTeam.route("/teams/update_team", methods=["POST"])
def update_team():
    repo = MySQLRepository()
    columns = repo.get_columns('constructors')
    form_data = request.form.to_dict()
    print(form_data)
    team_id = form_data.pop  ('constructorId', None)
    if team_id is not None:
            condition = {"constructorId": team_id}
            repo.update('constructors', form_data, condition)
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('teams.html', columns=columns, table_names=table_names,bool=False)

    


@viewTeam.route("/teams/delete_team/<int:team_id>", methods=["GET"])
def delete_team(team_id):
    repo = MySQLRepository()

    # Adding the new data to the teams table using repo method delete
    repo.delete('constructors', team_id, 'constructorId')
    
    # Redirect to the teams page after deleting
    return redirect(url_for('viewTeam.team_page'))