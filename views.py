from datetime import datetime

from read_tables import read_table, get_table_names

from flask import current_app, render_template, request

def home_page():
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

def table_page():
    table_name = "drivers"
    rows, cols = read_table(table_name)
    cols = [col[0] for col in cols]
    return render_template("tables.html", table=rows, title=table_name, columns=cols)
