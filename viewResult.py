from flask import Blueprint, render_template, current_app, request
from MySqlRepository import MySQLRepository

viewSeason = Blueprint('viewSeason', __name__)

viewSeason.route("/seasons", methods=["GET", "POST"])
def results_page():
    repo = MySQLRepository()  
    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        result_data = repo.read('results')
        columns = repo.get_columns('results')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('results.html', table_names=table_names)