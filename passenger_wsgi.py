import sys, os
cwd = os.getcwd()
sys.path.insert(0,cwd+'/kasawcu')
sys.path.append(cwd)
os.environ['DJANGO_SETTINGS_MODULE'] = "kasawcu.settings"
sys.stdout = sys.stderr
from paste.exceptions.errormiddleware import ErrorMiddleware
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
application = ErrorMiddleware(application, debug=True)
