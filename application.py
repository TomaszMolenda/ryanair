from flask import Flask, render_template, redirect, url_for, request

from scheduler import run_scheduler
from connector import check
import database

app = Flask(__name__)


@app.route('/')
def hello():
    trip = database.Database.getInstance().trip
    check()
    return render_template('index.html', trip=trip)


@app.route('/setup', methods=['GET'])
def setup_view():
    return render_template('setup.html')


@app.route('/setup', methods=['POST'])
def setup():
    database.Database.getInstance().destination = request.form['destination']
    database.Database.getInstance().origin = request.form['origin']
    return redirect(url_for('setup_view'))


@app.route('/all')
def all():
    countries = database.Database.getInstance().fetch()
    return render_template('all.html', countries=countries)


run_scheduler()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

