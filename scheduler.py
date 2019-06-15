from apscheduler.schedulers.background import BackgroundScheduler

import time
import atexit

from definition.service import ApplicationService


def run_scheduler():
    global scheduler

    def check_all_trips():
        application_service = ApplicationService.get_instance()
        application_service.check_trips_for_all_definition()

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=check_all_trips, trigger="interval", seconds=60)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
