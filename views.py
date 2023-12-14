from datetime import datetime

from read_tables import read_table

from flask import current_app, render_template

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

def table_page():
    table_name = "drivers"
    rows, cols = read_table(table_name)
    cols = [col[0] for col in cols]
    return render_template("tables.html", table=rows, title=table_name, columns=cols)
