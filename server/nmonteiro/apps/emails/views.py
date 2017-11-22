from django.views.generic import DetailView
from .models import PresentationEmail


class PresentationEmailDetail(DetailView):
    template_name = 'emails/email.html'
    model = PresentationEmail
    slug_field = 'hash'
    slug_url_kwarg = 'hash'
