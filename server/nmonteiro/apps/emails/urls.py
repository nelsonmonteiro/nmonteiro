from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^(?P<hash>\w+)/$', PresentationEmailDetail.as_view(), name='view_presentation_email'),
    url(r'^(?P<hash>\w+)/send/$', PresentationEmailSend.as_view(), name='send_presentation_email'),
]
