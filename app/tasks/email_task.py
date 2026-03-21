from app.core.celery_app import celery_app
import time


@celery_app.task
def send_user_email(user_email: str, user_id: int):
    # simulate sending email
    print(f"Sending registration confirmation to {user_email} for id {user_id}...")
    time.sleep(5)  # simulate delay
    print(f"Email sent to {user_email}!")
