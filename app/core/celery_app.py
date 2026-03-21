from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",  # Redis broker
    backend="redis://localhost:6379/1",  # optional result backend
    include=["app.tasks.email_task"],
)

# celery -A app.core.celery_app.celery_app worker --loglevel=info -P solo -E
celery_app.conf.beat_schedule = {
    "daily_user_report": {
        "task": "app.tasks.email_task.send_user_email",
        "schedule": crontab(hour=23, minute=9),  # every day at 9:00 AM
    },
    "weekly_report": {
        "task": "app.tasks.email_task.send_user_email",
        "schedule": crontab(hour=10, minute=30, day_of_week=1),  # every Monday
    },
}
celery_app.conf.enable_utc = False
celery_app.conf.timezone = "Asia/Singapore"  # type: ignore
