from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView, RedirectView
from robots_txt.views import RobotsTextView
from views import page_404, page_500
import conf

urlpatterns = patterns('',
    url(r'', include('favicon.urls')),
    url(r'^robots.txt$', RobotsTextView.as_view(template_name=conf.ROBOTS_TEMPLATE), name='site_robots_txt'),
    url(r'^test_page_404/$', page_404, name="page_404"),
    url(r'^test_page_500/$', page_500, name="page_500"),
)