from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.conf.urls.defaults import *
from research_platform import views
#import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'research_platform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^run/', 'research_platform.views.run', name='run')
)
