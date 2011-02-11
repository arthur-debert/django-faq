from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/(.*)', admin.site.urls), # administration
    url(r'^$', direct_to_template, {'template': 'index.html'}), # example page
    url(r'^faq/$', include('faq.urls')), # django-faq
)
