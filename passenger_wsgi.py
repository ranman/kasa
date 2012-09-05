import sys, os
sys.path.insert(0,'/home/wcu_kasa/env/bin/')
sys.path.insert(0,'/home/wcu_kasa/env/lib/python2.6/site-packages/Django-1.4-py2.6.egg-info')
sys.path.insert(0,'/home/wcu_kasa/env/lib/python2.6/site-packages/')
cwd = os.getcwd()
sys.path.insert(0,cwd+'/kasawcu')
sys.path.append(cwd)
os.environ['DJANGO_SETTINGS_MODULE'] = "kasawcu.settings"
sys.stdout = sys.stderr
from paste.exceptions.errormiddleware import ErrorMiddleware
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
application = ErrorMiddleware(application, debug=True)
