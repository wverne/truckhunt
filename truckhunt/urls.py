from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('truckhunt.views',
                       (r'^$',       'homepage'),
                       (r'^trucks/$', 'trucks_page'),
                       (r'^types/$', 'types_page'),
                       (r'^featured/$', 'featured_page'),
                       (r'^map_test/$', 'map_test_page'),
    # Examples:
    # url(r'^$', 'truckhunt.views.home', name='home'),
    # url(r'^truckhunt/', include('truckhunt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
