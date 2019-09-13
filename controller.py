import firebase_admin
import logging
from firebase_admin import credentials
from flask import Flask, render_template, redirect, url_for, request

from definition.query import DefinitionQuery
from email_query import EmailQuery
from email_service import EmailApplicationService
from scheduler import run_scheduler
from definition.service import ApplicationService
from trip.query import TripQuery

app = Flask(__name__)

database_url = {'databaseURL': "https://ryanair-a33cd.firebaseio.com/"}
cred = credentials.Certificate("ryanair-a33cd-firebase-adminsdk-jd0w3-595816bfc2.json")
firebase_admin.initialize_app(cred, database_url)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/definitions', methods=['GET'])
def list_definitions_view():

    definition_query = DefinitionQuery.get_instance()
    definitions = definition_query.list_all()

    return render_template('definitions.html', definitions=definitions)


@app.route('/definitions/add', methods=['GET'])
def add_definitions_view():
    return render_template('definitions-add.html')


@app.route('/definitions', methods=['POST'])
def add_definitions_action():

    application_service = ApplicationService.get_instance()
    application_service.save_definition(request)

    return redirect(url_for('list_definitions_view'))


@app.route('/definitions/<definition_id>/delete', methods=['POST'])
def delete_definition_action(definition_id):

    application_service = ApplicationService.get_instance()
    application_service.delete_definition(definition_id)

    return redirect(url_for('list_definitions_view'))


@app.route('/definitions/<definition_id>/check-trips', methods=['POST'])
def check_definition_trips_action(definition_id):

    application_service = ApplicationService.get_instance()
    application_service.check_trips(definition_id)

    return redirect(url_for('list_definitions_view'))


@app.route('/definitions/<definition_id>/trips', methods=['GET'])
def list_definitions_trips_view(definition_id):

    trip_query = TripQuery.get_instance()
    definition_query = DefinitionQuery.get_instance()

    definition = definition_query.get(definition_id)
    trips = trip_query.list_by_definition(definition)

    return render_template('trips.html', definition=definition, trips=trips)


@app.route('/email', methods=['GET'])
def get_email_view():

    email_query = EmailQuery.get_instance()
    email = email_query.get()

    return render_template('email.html', email=email)


@app.route('/email', methods=['POST'])
def set_email_action():

    email_application_service = EmailApplicationService.get_instance()
    email_application_service.set_email(request)

    return redirect(url_for('index'))


run_scheduler()


if __name__ == '__main__':
    logging.basicConfig(filename='application.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    app.run(host="0.0.0.0")

