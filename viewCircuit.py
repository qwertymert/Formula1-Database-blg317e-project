from flask import Blueprint, render_template, request, redirect, url_for, flash
import MySqlRepository

viewCircuit = Blueprint('viewCircuit', __name__, template_folder='templates')

@viewCircuit.route('/circuits', methods=['GET', 'POST'])
def circuits_page():
    repo = MySqlRepository.MySQLRepository()

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        circuits_data = repo.read('circuits')
        columns = repo.get_columns('circuits')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('circuits.html', circuits_data=circuits_data, columns=columns, table_names=table_names)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('circuits.html', table_names=table_names)
