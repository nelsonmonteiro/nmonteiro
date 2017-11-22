import string
from tinymce.models import HTMLField
from django.db import models
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

    header = HTMLField(null=True, blank=True)
    footer = HTMLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.hash:
            while not self.hash or PresentationEmail.objects.filter(hash=self.hash).exclude(id=self.id):
                self.hash = get_random_string(length=15, allowed_characters=string.ascii_letters)
        super(PresentationEmail, self).save(*args, **kwargs)

    def send(self):
        pass

    def __str__(self):
        return self.identification
