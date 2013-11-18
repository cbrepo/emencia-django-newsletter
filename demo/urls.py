"""Urls for the demo of emencia.django.newsletter"""
import os

from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import handler404
from django.conf.urls import handler500
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', TemplateView.as_view(template_name='/admin/')),
                       url(r'^newsletters/', include('emencia.django.newsletter.urls')),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += patterns('django.views.static',
                        url(r'^edn/(?P<path>.*)$', 'serve',
                            {'document_root': os.path.join(os.path.dirname(__file__),
                                                           '..', 'emencia', 'django',
                                                           'newsletter', 'media', 'edn')}),)
