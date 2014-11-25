from django.conf.urls import patterns, include, url
from django.contrib import admin
from research_platform import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'research_platform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^runcommand/', 'research_platform.views.runcommand', name='runcommand'),
)
