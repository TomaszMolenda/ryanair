import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template, redirect, url_for, request

from dto import DefinitionDto
from scheduler import run_scheduler
from connector import check

app = Flask(__name__)

database_url = {'databaseURL': "https://ryanair-a33cd.firebaseio.com/"}
cred = credentials.Certificate("/home/tomo/Downloads/ryanair-a33cd-firebase-adminsdk-jd0w3-4a43b990c3.json")
firebase_admin.initialize_app(cred, database_url)


@app.route('/')
def hello():
    definitions = db.reference().child('definitions').get()
    for definition_id, definition in definitions.items():
        check(definition_id, definition)

    return render_template('index.html', definitions=definitions)


@app.route('/definitions', methods=['GET'])
def definitions():
    list = []
    definitions = db.reference().child('definitions').get()
    for definition_id, definition in definitions.items():
        list1 = []
        for trip_id, trip in definition['trips'].items():
            list1.append(trip)
        defi = DefinitionDto(definition, list1)
        list.append(defi)
    return render_template('definitions.html', definitions=list)


@app.route('/definitions/add', methods=['GET'])
def add_definitions_view():
    return render_template('definitions-add.html')


@app.route('/definitions', methods=['POST'])
def add_trips():
    root = db.reference()
    root.child('definitions').push(
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
    return redirect(url_for('add_definitions_view'))


run_scheduler()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

