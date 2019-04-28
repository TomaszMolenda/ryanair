from flask import Flask, render_template, redirect, url_for, request

from scheduler import run_scheduler
from connector import check
import database

app = Flask(__name__)


@app.route('/')
def hello():
    check()
    checked_trips = database.Database.getInstance().checked_trips
    return render_template('index.html', checked_trips=checked_trips)


@app.route('/setup', methods=['GET'])
def setup_view():
    return render_template('setup.html')


@app.route('/setup', methods=['POST'])
def setup():
    database.Database.getInstance().destination = request.form['destination']
    database.Database.getInstance().departure_date = request.form['departure_date']
    database.Database.getInstance().origin = request.form['origin']
    database.Database.getInstance().arrival_date = request.form['arrival_date']
    database.Database.getInstance().adult = request.form['adult']
    database.Database.getInstance().teen = request.form['teen']
    database.Database.getInstance().child = request.form['child']
    database.Database.getInstance().flex_days = request.form['flex_days']
    return redirect(url_for('setup_view'))


run_scheduler()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

