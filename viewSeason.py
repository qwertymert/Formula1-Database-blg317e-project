from flask import Blueprint, render_template, current_app, request,redirect,url_for, url_for
from MySqlRepository import MySQLRepository

viewSeason = Blueprint('viewSeason', __name__)

@viewSeason.route("/seasons", methods=["GET", "POST"])
def seasons_page():
    repo = MySQLRepository()  

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all seasons
        seasons_data = repo.read('seasons')
        columns = repo.get_columns('seasons')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('seasons.html', seasons_data=seasons_data, columns=columns, table_names=table_names)
    else:
        # Otherwise, fetch a limited number of seasons (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('seasons.html', table_names=table_names)


@viewSeason.route("/seasons/add_season", methods=["POST"])
def add_season():
    repo = MySQLRepository()

    # Getting all new data for all columns
    columns = repo.get_columns('seasons')
    data_to_add = {column: request.form.get(column) for column in columns}

    # Adding the new data to the seasons table using repo method create
    repo.create('seasons', data_to_add)
    seasons_data = repo.read('seasons')
    columns = repo.get_columns('seasons')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('seasons.html', seasons_data=seasons_data, columns=columns, table_names=table_names)
    


@viewSeason.route("/seasons/delete_season/<int:year>", methods=["GET"])
def delete_season(year):
    repo = MySQLRepository()

    # Adding the new data to the seasons table using repo method delete
    repo.delete('seasons', year, 'year')
    
    # Redirect to the seasons page after deleting
    return redirect(url_for('viewSeason.seasons_page'))
