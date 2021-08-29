from apscheduler.schedulers.background import BackgroundScheduler
from .something_update import abc


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(abc, 'interval',hours=7)
    scheduler.start()