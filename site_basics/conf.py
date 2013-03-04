import os

from django.conf import settings

ROBOTS_TEMPLATE = getattr(settings, 'ROBOTS_TEMPLATE', 'robots.txt')