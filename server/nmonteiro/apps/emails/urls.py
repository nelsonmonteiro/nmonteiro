from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^(?P<hash>\w+)/$', PresentationEmailDetail.as_view()),
]
