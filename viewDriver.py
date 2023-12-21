from MySqlRepository import MySQLRepository
import views

from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app


viewDriver = Blueprint('viewDriver', __name__)

@viewDriver.route('/drivers',methods=['GET', 'POST'])
def drivers_page():
    if request.method == 'POST':
        repo = MySQLRepository()
        table_name = "drivers"
        rows, cols = views.select_table(table_name)
        cols = [col[0] for col in cols]
        return render_template("drivers.html", table=rows, title=table_name, columns=cols)
    else:
        return render_template("drivers.html")
