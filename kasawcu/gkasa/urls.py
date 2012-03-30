from django.conf.urls.defaults import *
from kasawcu.gkasa.models import Student

urlpatterns = patterns('kasawcu.gkasa.views',
    (r'^$', 'detail'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^(?P<student_id>\d+)/report/$', 'report'),
)
