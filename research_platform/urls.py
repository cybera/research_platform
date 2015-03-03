from django.conf.urls import patterns, include, url
from django.contrib import admin
from research_platform import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'research_platform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^runcommand/', 'research_platform.views.runcommand', name='runcommand'),
	url(r'^createvm/', 'research_platform.views.createvm', name='createvm'),
	url(r'^uploadfile/', 'research_platform.views.upload_file', name='uploadfile'),
	url(r'^success/', 'research_platform.views.success', name='success')
)
