from flask import Flask, render_template, request, redirect, url_for, flash
import views
import mysql.connector
import os
import yaml


def create_app():
    app = Flask(__name__)
    app.add_url_rule("/", view_func=views.home_page)   
    app.add_url_rule("/tables", view_func=views.table_page) 
    # app.add_url_rule("/alter_movie/<movie_id>", view_func=views.alter_movie)
    # app.add_url_rule("/un_alter_movie/<movie_id>", view_func=views.un_alter_movie)

    ### TODO-1: ADD url rule for delete_movie function in the views.py
    # app.add_url_rule("/delete_movie/<movie_id>", view_func=views.delete_movie)
    
    # Connect to MySQL
    
    # os.system("python create_tables.py")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)