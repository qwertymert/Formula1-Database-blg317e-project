from flask import Blueprint, render_template, request, redirect, url_for, flash
import MySqlRepository

viewCircuit = Blueprint('viewCircuit', __name__, template_folder='templates')

@viewCircuit.route('/circuits', methods=['GET', 'POST'])
def circuits_page():
    repo = MySqlRepository.MySQLRepository()
    columns = repo.get_columns('circuits')
    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all circuits
        circuits_data = repo.read('circuits')
        
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('circuits.html', circuits_data=circuits_data, columns=columns, table_names=table_names,bool=True)
    else:
        # Otherwise, fetch a limited number of circuits (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('circuits.html', columns=columns, table_names=table_names,bool=False)


@viewCircuit.route('/circuits/filter_data', methods=['POST'])
def filter_data():
    repo = MySqlRepository.MySQLRepository()

    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')

    circuits_data = repo.read('circuits',filter, column)
    columns = repo.get_columns('circuits')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('circuits.html', circuits_data=circuits_data, columns=columns, table_names=table_names,bool=True )

@viewCircuit.route("/circuits/add_circuits", methods=["POST"])
def add_circuits():
    repo = MySqlRepository.MySQLRepository()

    # Getting all new data for all columns
    columns = repo.get_columns('circuits')[1:]
    data_to_add = {column: request.form.get(column) for column in columns}

    # Adding the new data to the teams table using repo method create
    repo.create('circuits', data_to_add)
    circuits_data = repo.read('circuits')
    columns = repo.get_columns('circuits')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('circuits.html', circuits_data=circuits_data, columns=columns, table_names=table_names,bool=False)


@viewCircuit.route("/circuits/update_circuits", methods=["POST"])
def update_circuits():
    repo = MySqlRepository.MySQLRepository()
    columns = repo.get_columns('circuits')
    form_data = request.form.to_dict()
    print(form_data)
    id = form_data.pop  ('circuitId', None)
    if id is not None:
            condition = {"circuitId": id}
            repo.update('circuits', form_data, condition)
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('circuits.html', columns=columns, table_names=table_names,bool=False)

@viewCircuit.route("/circuits/delete_circuits/<int:circuit_id>", methods=["POST"])
def delete_circuit(circuit_id):
    repo = MySqlRepository.MySQLRepository()
    repo.delete('circuits', circuit_id, 'circuitId')

    return redirect(url_for('viewCircuit.circuits_page'))