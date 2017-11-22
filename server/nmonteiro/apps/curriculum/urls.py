from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', CurriculumDetail.as_view()),
    url(r'^personal-information/$', PersonalInformationDetail.as_view()),
]
