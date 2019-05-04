import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template, redirect, url_for, request
from scheduler import run_scheduler
from connector import check
import database

app = Flask(__name__)

database_url = {'databaseURL': "https://ryanair-a33cd.firebaseio.com/"}
cred = credentials.Certificate("/home/tomo/Downloads/ryanair-a33cd-firebase-adminsdk-jd0w3-4a43b990c3.json")
firebase_admin.initialize_app(cred, database_url)


@app.route('/')
def hello():
    check()
    checked_trips = database.Database.getInstance().checked_trips
    return render_template('index.html', checked_trips=checked_trips)


@app.route('/setup', methods=['GET'])
def setup_view():
    setup = db.reference().child('setup').get()
    return render_template('setup.html', setup=setup)


@app.route('/setup', methods=['POST'])
def setup():
    root = db.reference()
    root.child('setup').set(
        {
            'destination': request.form['destination'],
            'departure_date': request.form['departure_date'],
            'origin': request.form['origin'],
            'arrival_date': request.form['arrival_date'],
            'adult': request.form['adult'],
            'teen': request.form['teen'],
            'child': request.form['child'],
            'flex_days': request.form['flex_days']
        }
    )
    return redirect(url_for('setup_view'))


run_scheduler()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

