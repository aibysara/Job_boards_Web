from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_contact_email_task(self, subject, message, from_email):
    try:
        send_mail(
            subject,
            message,
            from_email,
            ['thesni.inform@gmail.com'],  # Admin email
            fail_silently=False,
        )
        logger.info(f"Email sent successfully: {subject}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        raise self.retry(exc=e, countdown=60)  # Retry task in case of failure


