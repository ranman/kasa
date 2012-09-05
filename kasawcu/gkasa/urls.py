from django.conf.urls import patterns, include, url
from kasawcu.gkasa.models import Student

urlpatterns = patterns('kasawcu.gkasa.views',
    (r'^$', 'detail'),
    (r'^(?P<student_id>\d+)/report/$', 'report'),
)
