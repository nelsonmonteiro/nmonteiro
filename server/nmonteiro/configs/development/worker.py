from __future__ import absolute_import

import os
import sys
from celery import Celery
from django.conf import settings

# we want a few paths on the python path
# first up we add the root above the application so
# we can have absolute paths everywhere
python_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../../'
)
# we have have a local apps directory
apps_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../'
)

# we add them first to avoid any collisions
sys.path.insert(0, python_path)
sys.path.insert(0, apps_path)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('nmonteiro_server')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


