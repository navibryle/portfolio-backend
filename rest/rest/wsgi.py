"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os 
import time 
import traceback 
import signal 
import sys 

#two paths appended so apache recognizes the python version in the virtual env
sys.path.append('var/www/backend')
sys.path.append('var/www/backedn/rest/rest')
sys.path.append('/var/www/backend/rest')
sys.path.append('/var/www/backend/lib/python3.6/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')

application = get_wsgi_application() 
