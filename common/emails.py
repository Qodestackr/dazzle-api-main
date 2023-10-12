
# MailHog => util function to test sending email

# Model signals

'''
Celery Beat => send tasks periodically 
'''
# CELERY::pip install celery[redis] django-celery-beat django-celery-results


'''
You can use Django signals to send emails automatically when certain events occur, 
such as user registration or password reset. 
For example, you can send a welcome email to users when they register.
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Site'
        message = 'Thank you for registering!'
        from_email = 'admin@example.com'
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)

'''
