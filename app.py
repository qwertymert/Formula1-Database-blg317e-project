from flask import Flask
from views import views, viewDriver, viewSeason, viewResult, viewRace, viewTeam, viewCircuit
import yaml
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = "abc"
    
    yaml_config = {"user": "root", "password": "",
                   "host": "localhost", "database": "formula1"}
    yaml.dump(yaml_config, open('db.yaml', "w"))
    
    app.config["SUCCESSFUL_LOGIN"] = False
    
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/login_page", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/select_table", view_func=views.select_table, methods=["GET", "POST"])
    app.add_url_rule("/filter_table", view_func=views.filter_table, methods=["GET", "POST"])
    app.add_url_rule("/drivers", view_func=viewDriver.drivers_page, methods=["GET", "POST"])
    app.add_url_rule("/seasons", view_func=viewSeason.seasons_page, methods=["GET", "POST"])
    app.add_url_rule("/results", view_func=viewResult.results_page, methods=["GET", "POST"])
    app.add_url_rule("/races",view_func=viewRace.races_page, methods=["GET", "POST"])
    app.add_url_rule("/teams", view_func=viewTeam.teams_page, methods=["GET", "POST"])
    app.add_url_rule("/circuits", view_func=viewCircuit.circuits_page, methods=["GET", "POST"])

    app.register_blueprint(viewDriver.viewDriver, url_prefix='/')
    app.register_blueprint(viewSeason.viewSeason, url_prefix='/')
    app.register_blueprint(viewResult.viewResult, url_prefix='/')
    app.register_blueprint(viewRace.viewRace, url_prefix='/')
    app.register_blueprint(viewTeam.viewTeam, url_prefix='/')
    app.register_blueprint(viewCircuit.viewCircuit, url_prefix='/')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    try:
        os.remove('db.yaml')
        print("Database connection closed.")
    except:
        print("Application closed.")