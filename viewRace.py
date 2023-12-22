from flask import Blueprint, render_template, current_app, request
import MySqlRepository

viewRace = Blueprint('viewRace', __name__)

@viewRace.route("/races", methods=["GET", "POST"])
def races_page():
    repo = MySqlRepository.MySQLRepository()

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        races_data = repo.read('races')
        columns = repo.get_columns('races')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('races.html', races_data=races_data, columns=columns, table_names=table_names)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('races.html', table_names=table_names)
