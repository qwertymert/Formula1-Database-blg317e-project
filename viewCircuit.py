from flask import Blueprint, render_template, request
import MySqlRepository

viewCircuit = Blueprint('viewCircuit', __name__, template_folder='templates')
repo = MySqlRepository.MySQLRepository()

# Inside your Flask route for updating circuits
@viewCircuit.route('/circuits', methods=['POST'])
def circuits_page():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        circuit_id = form_data.pop('circuitId', None)

        if circuit_id is not None:
            # Construct the condition for the update
            condition = {"circuitId": circuit_id}
            
            # Update the database
            repo.update('circuits', form_data, condition)

    # Rest of your code to fetch and display circuits
    circuits_data = repo.read('circuits')
    columns = repo.get_columns('circuits')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]

    return render_template('circuits.html', circuits_data=circuits_data, columns=columns, table_names=table_names)
