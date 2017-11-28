from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='valispace/functions.html')),
    url(r'^list/$', FunctionsList.as_view()),
    url(r'^create/$', FunctionCreate.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', FunctionDestroy.as_view()),
    url(r'^parse/$', FunctionParseView.as_view()),
]
