from django import http
from django.urls import reverse
from django.views.generic import DetailView
from .models import PresentationEmail


class PresentationEmailDetail(DetailView):
    template_name = 'emails/email.html'
    model = PresentationEmail
    slug_field = 'hash'
    slug_url_kwarg = 'hash'

    def get_context_data(self, **kwargs):
        context = super(PresentationEmailDetail, self).get_context_data(**kwargs)
        context['send_button'] = True
        return context


class PresentationEmailSend(DetailView):
    template_name = 'emails/sent.html'
    model = PresentationEmail
    slug_field = 'hash'
    slug_url_kwarg = 'hash'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = request.user

        if not (user.is_authenticated() and user.is_superuser):
            return http.HttpResponseRedirect(
                reverse('view_presentation_email', kwargs={'hash': self.object.hash}))

        self.object.send_email()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
