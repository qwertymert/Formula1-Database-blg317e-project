from flask import Blueprint, render_template, current_app, request
import MySqlRepository

viewTeam = Blueprint('viewTeam', __name__)  

@viewTeam.route("/teams", methods=["GET", "POST"])
def teams_page():
    repo = MySqlRepository.MySQLRepository()
    columns = repo.get_columns('constructors')

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        teams_data = repo.read('constructors')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names,bool=True)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('teams.html', columns=columns, table_names=table_names,bool=False)
    
@viewTeam.route("/teams/filter_data", methods=["POST"])
def filter_data():
    repo = MySqlRepository.MySQLRepository()

    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')


    teams_data = repo.read('constructors',filter, column)
    columns = repo.get_columns('constructors')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names,bool=True)