from apscheduler.schedulers.background import BackgroundScheduler

import time
import atexit


def run_scheduler():
    global scheduler

    def print_date_time():
        t = time.strftime("%A, %d. %B %Y %I:%M:%S %p")
        print(t)

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
