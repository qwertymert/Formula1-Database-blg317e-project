from flask import Flask, render_template, request, redirect, url_for, flash
import views
import viewDriver
import viewSeason
import viewResult
import viewRace
import viewTeam
import viewCircuit
import mysql.connector
import os
import yaml


def create_app():
    app = Flask(__name__)

    app.add_url_rule("/", view_func=views.home_page)
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
