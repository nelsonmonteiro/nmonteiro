import string
import datetime
import pytz
from tinymce.models import HTMLField
from django.db import models
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.encoding import python_2_unicode_compatible
from apps.core.utils.models import BaseModel
from apps.core.utils.crypto import get_random_string


@python_2_unicode_compatible
class PresentationEmail(BaseModel):
    identification = models.CharField(max_length=150, help_text='Company and reason')

    hash = models.CharField(max_length=15, db_index=True, unique=True)
    email = models.EmailField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)
    sent_date = models.DateTimeField(null=True, blank=True)

    subject = models.CharField(max_length=150, null=True, blank=True)
    header = HTMLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.hash:
            while not self.hash or PresentationEmail.objects.filter(hash=self.hash).exclude(id=self.id):
                self.hash = get_random_string(length=15, allowed_characters=string.ascii_letters)
        super(PresentationEmail, self).save(*args, **kwargs)

    def send_email(self):
        if not self.is_sent and self.email and self.subject:
            message = 'Hi there! You are not able to receive html content on your email.' \
                      'Please go to %s to see your message. \n\n Thank you and best regards. \n' \
                      'Nelson.' % reverse('send_presentation_email', kwargs={'hash': self.hash})
            html = render_to_string('emails/email.html', {'object': self, 'settings': settings})
            send_mail(self.subject, message, settings.DEFAULT_FROM_EMAIL, [self.email], html_message=html)
            self.is_sent = True
            self.sent_date = datetime.datetime.now(tz=pytz.UTC)
            self.save()

    def __str__(self):
        return self.identification
