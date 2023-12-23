from flask import Blueprint, render_template, current_app, request
import MySqlRepository

viewTeam = Blueprint('viewTeam', __name__)  

@viewTeam.route("/teams", methods=["GET", "POST"])
def teams_page():
    repo = MySqlRepository.MySQLRepository()

    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        form_data = request.form.to_dict()
        print(form_data)
        constructor_id = form_data.pop('constructorId', None)

        if constructor_id is not None:
            # Construct the condition for the update
            condition = {"constructorId": constructor_id}
            repo.update('constructors', form_data, condition)
        
    teams_data = repo.read('constructors')
    columns = repo.get_columns('constructors')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('teams.html', teams_data=teams_data, columns=columns, table_names=table_names)
