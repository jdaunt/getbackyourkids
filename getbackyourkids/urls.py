from django.conf.urls import patterns, include, url
from getbackyourkids.view import gbyk, gbykbonus, gbykcomments

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', gbyk),
	url(r'^gbyk/$', gbyk),
	url(r'^gbykbonus/$', gbykbonus),
	url(r'^gbykcomments/$', gbykcomments),
	# Uncomment the admin/doc line below to enable admin documentation:
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
