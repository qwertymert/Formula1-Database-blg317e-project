from flask import Blueprint, render_template, current_app, request
from MySqlRepository import MySQLRepository

viewResult = Blueprint('viewResult', __name__)

@viewResult.route("/results", methods=["GET", "POST"])
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
    
@viewResult.route("/results/filter_data", methods=["POST"])
def filter_data():
    repo = MySQLRepository()

    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')


    result_data = repo.read('results',filter, column)
    columns = repo.get_columns('results')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names)

@viewResult.route("/results/add_result", methods=["POST"])
def add_result():
    repo = MySQLRepository()

    # Getting all new data for all columns
    columns = repo.get_columns('results')[1:]
    data_to_add = {column: request.form.get(column) for column in columns}

    # Adding the new data to the teams table using repo method create
    repo.create('results', data_to_add)
    result_data = repo.read('results')
    columns = repo.get_columns('results')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names)