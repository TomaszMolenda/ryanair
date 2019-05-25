import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template, redirect, url_for, request

from dto import DefinitionDto
from query import DefinitionQuery
from scheduler import run_scheduler
from connector import check
from service import ApplicationService

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


run_scheduler()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

