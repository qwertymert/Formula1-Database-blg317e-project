from datetime import datetime

from read_tables import read_table, get_table_names, read_columns

from filter_tables import filter_table_and_column

from flask import render_template, request

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

# def table_page():
#     table_name = "drivers"
#     rows, cols = read_table(table_name)
#     cols = [col[0] for col in cols]
#     return render_template("tables.html", table=rows, title=table_name, columns=cols)

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