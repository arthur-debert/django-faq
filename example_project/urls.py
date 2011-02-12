from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)), # administration
    url(r'^$', TemplateView.as_view(template_name="index.html")), # example page
    url(r'^faq/', include('faq.urls')), # django-faq
)
