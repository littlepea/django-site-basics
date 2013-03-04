from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView, RedirectView
from robots_txt.views import RobotsTextView
import conf

urlpatterns = patterns('',
    url(r'', include('favicon.urls')),
    url(r'^robots.txt$', RobotsTextView.as_view(template_name=conf.ROBOTS_TEMPLATE)),
)