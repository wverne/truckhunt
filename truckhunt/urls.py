from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('truckhunt.views',
                       (r'^$',       'homepage'),
                       (r'^trucks/$', 'trucks_page'),
                       (r'^trucks/(.+)/$', 'trucks_page'),
                       (r'^featured/$', 'featured_page'),
                       (r'^about/$', 'about_page'),
                       (r'^login/$', 'login_view'),
                       (r'^logout/$', 'logout_view'),
                       (r'^disabled_account/$', 'disabled_page'),
                       (r'^invalid_login/$', 'invalid_login_page'),
                       (r'^user/(.+)/$', 'user_page'),
                      )

urlpatterns += patterns('',
                        (r'^admin/', include(admin.site.urls)),
                        (r'^static/(.+)$', 
                         'django.views.static.serve', 
                         {'document_root': settings.STATIC_ROOT}),

        # Uncomment the admin/doc line below to enable admin documentation
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       )
