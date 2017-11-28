from django.conf.urls import url, include


urlpatterns = [
    url(r'^functions/', include('apps.valispace.functions.urls')),
]
