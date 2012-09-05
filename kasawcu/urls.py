from django.conf.urls import patterns, include, url 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^gkasa/', include('kasawcu.gkasa.urls')),
    (r'^ugkasa/', include('kasawcu.ugkasa.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
#    (r'^$', 'kasawcu.views.index'), 
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
