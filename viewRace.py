from flask import Blueprint, redirect, render_template, current_app, request, url_for
from MySqlRepository import MySQLRepository

viewRace = Blueprint('viewRace', __name__)
repo = MySQLRepository()

@viewRace.route("/races", methods=["GET", "POST"])
def races_page():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        print(form_data)
        driver_id = form_data.pop  ('raceId', None)

        if driver_id is not None:
            condition = {"raceId": driver_id}
            repo.update('races', form_data, condition)

    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('races.html', table_names=table_names)
  
@viewRace.route("/races/filter_data", methods=["POST"])
def filter_data():
    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')


    races_data = repo.read('races',filter, column)
    columns = repo.get_columns('races')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('races.html', races_data=races_data, columns=columns, table_names=table_names)

@viewRace.route("/races/delete/<int:race_id>", methods=["POST"])
def delete_race(race_id):
    # Delete the race from the database
    print('delete', race_id);
    repo.delete('races', {"raceId": race_id})

    return redirect(url_for('viewRace.races_page'))