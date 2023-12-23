from flask import Blueprint, render_template, request
import MySqlRepository

viewSeason = Blueprint('viewSeason', __name__, template_folder='templates')
repo = MySqlRepository.MySQLRepository()

# Inside your Flask route for updating seasons
@viewSeason.route('/seasons', methods=['POST'])
def seasons_page():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        print(form_data)
        year = form_data.pop('year', None)

        if year is not None:
            # Construct the condition for the update
            condition = {"year": year}
            repo.update('seasons', form_data, condition)

    # Rest of your code to fetch and display seasons
    seasons_data = repo.read('seasons')
    columns = repo.get_columns('seasons')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]

    return render_template('seasons.html', seasons_data=seasons_data, columns=columns, table_names=table_names)
