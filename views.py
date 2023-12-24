from datetime import datetime

from read_tables import read_table, get_table_names, read_columns, check_connection

from filter_tables import filter_table_and_column

from flask import render_template, request, flash, redirect, url_for
from flask import current_app as app
import yaml

# view function for login page where after inputting mysql username and password, the user is redirected to the home page
def login_page():
    if request.method == "POST" and not app.config["SUCCESSFUL_LOGIN"]:
        # getting input with name = username in HTML
        username = request.form.get("username")
        # getting input with name = password in HTML
        password = request.form.get("password")
    
        db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
        db_config['user'] = username
        db_config['password'] = password
        yaml.dump(db_config, open('db.yaml', "w"))
        connection = check_connection()
        
        if not connection:
            db_config['user'] = "root"
            db_config['password'] = ""
            yaml.dump(db_config, open('db.yaml', "w"))
                
        if connection:
            app.config["SUCCESSFUL_LOGIN"] = True
            flash('You were successfully logged in')
            
            return render_template("home.html")
        else:
            flash('Incorrect MYSQL username or password. Please try again.')
            return render_template("login.html")
    
    return render_template("login.html")
    
def home_page():
    if not app.config["SUCCESSFUL_LOGIN"]:
        return redirect(url_for('login_page'))
    else:
        today = datetime.today()
        day_name = today.strftime("%A")
        return render_template("home.html", day=day_name)

def select_table():
    names = get_table_names()
    names = [name[0] for name in names]
    
    if request.method == "POST":
        # getting input with name = table-name in HTML
        table_name = request.form.get("table-name")
        rows, cols = read_table(table_name)
        cols = [col[0] for col in cols]
        
        return render_template("select_table.html", table=rows, title=table_name, columns=cols, table_names=names)
    
    return render_template("select_table.html", table_names=names)

def filter_table():
    names = get_table_names()
    names = [name[0] for name in names]
    
    if request.method == "POST":
        
        
        # check if reset button was pressed
        if "reset" in request.form:
            return render_template("filter_table.html", table_names=names)
        
        # getting input with name = table-name in HTML
        table_name = request.form.get("table-name")
        
        cols = read_columns(table_name)
        cols = [col[0] for col in cols]
        
        # getting input with name = table-name in HTML
        column_name = request.form.get("column-name")
        
        if column_name is None:
            return render_template("filter_table.html", title=table_name, columns=cols, table_names=names, default_table=table_name)
        
        value = request.form.get("filter")
        if value is None:
            return render_template("filter_table.html", title=table_name, column_name=column_name, columns=cols, table_names=names, default_table=table_name, default_column=column_name)
        
        # value can be a string or a number, so filter with SQL accordingly
        if value.isnumeric():
            rows = filter_table_and_column(table_name, column_name, value, "number")
        else:
            rows = filter_table_and_column(table_name, column_name, value, "string")
        
        return render_template("filter_table.html", table=rows, title=table_name, column_name=column_name, columns=cols, table_names=names, default_table=table_name, default_column=column_name)
    
    
    return render_template("filter_table.html", table_names=names)