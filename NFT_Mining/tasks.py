import logging
 
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celery import app
 
 
@app.task
def send_verification_email(user_id):
    print("TASK SAMPLE")
