from flask import Blueprint, redirect, render_template, current_app, request, url_for
from MySqlRepository import MySQLRepository

viewResult = Blueprint('viewResult', __name__)

@viewResult.route("/results", methods=["GET", "POST"])
def results_page():
    repo = MySQLRepository()  
    columns = repo.get_columns('results')
    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all results
        result_data = repo.read('results')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names,bool=True)
    else:
        # Otherwise, fetch a limited number of results (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('results.html', columns=columns, table_names=table_names,bool=False)
    
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
    return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names,bool=True)

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
    return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names,bool=False)

@viewResult.route("/results/update_result", methods=["POST"])
def update_result():
    repo = MySQLRepository()
    columns = repo.get_columns('results')
    form_data = request.form.to_dict()
    print(form_data)
    result_id = form_data.pop  ('resultId', None)
    if result_id is not None:
            condition = {"resultId": result_id}
            repo.update('results', form_data, condition)
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('results.html', columns=columns, table_names=table_names,bool=False)

    


@viewResult.route("/results/delete_result/<int:result_id>", methods=["GET"])
def delete_result(result_id):
    repo = MySQLRepository()

    # Adding the new data to the results table using repo method delete
    repo.delete('results', result_id, 'resultId')
    
    # Redirect to the results page after deleting
    return redirect(url_for('viewResult.results_page'))