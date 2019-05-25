from apscheduler.schedulers.background import BackgroundScheduler
from firebase_admin import db
from connector import check

import time
import atexit


def run_scheduler():
    global scheduler

    def print_date_time():
        t = time.strftime("%A, %d. %B %Y %I:%M:%S %p")
        definitions = db.reference().child('definitions').get()
        for definition_id, definition in definitions.items():
            check(definition_id, definition)
        print(t)

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=60)
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
