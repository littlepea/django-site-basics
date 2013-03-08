import os

from django.conf import settings

ugettext = lambda s: s

ROBOTS_TEMPLATE = getattr(settings, 'ROBOTS_TEMPLATE', 'robots.txt')

ERROR_PAGE_THEMES = ('annanta', 'robotik')

ERROR_PAGE_COLORS = (
    ('blue', 'grey', 'red', 'brown', 'green'),
    ('blue', 'gray', 'green'),
)

ERROR_PAGE_THEME = getattr(settings, 'ERROR_PAGE_THEME', ERROR_PAGE_THEMES[0])

ERROR_PAGE_THEME_COLOR = getattr(settings, 'ERROR_PAGE_THEME_COLOR', ERROR_PAGE_COLORS[0][0])

ERROR_PAGE_THEME_STATIC_URL = getattr(settings, 'ERROR_PAGE_THEME_STATIC_URL', '%s%s/%s/' % (
                                                                        settings.STATIC_URL,
                                                                        'site_basics',
                                                                        ERROR_PAGE_THEME
))

ERROR_404_PAGE_TEMPLATE = getattr(settings, 'ERROR_404_PAGE_TEMPLATE', '%s/404.html' % ERROR_PAGE_THEME)

ERROR_500_PAGE_TEMPLATE = getattr(settings, 'ERROR_500_PAGE_TEMPLATE', '%s/500.html' % ERROR_PAGE_THEME)

ERROR_PAGE_LOGO_URL = getattr(settings, 'ERROR_PAGE_LOGO_URL', None)

ERROR_PAGE_NAV_LINKS = getattr(settings, 'ERROR_PAGE_NAV_LINKS', (
    ('/', ugettext('Home')),
))

ERROR_PAGE_CMS_LINKS = getattr(settings, 'ERROR_PAGE_CMS_LINKS', False)

ERROR_PAGE_SOCIAL_LINKS = getattr(settings, 'ERROR_PAGE_SOCIAL_LINKS', ())

ERROR_PAGE_SEARCH_ACTION = getattr(settings, 'ERROR_PAGE_SEARCH_ACTION', None)

ERROR_PAGE_SEARCH_METHOD = getattr(settings, 'ERROR_PAGE_SEARCH_METHOD', 'GET')

ERROR_PAGE_SEARCH_PARAM = getattr(settings, 'ERROR_PAGE_SEARCH_PARAM', 'q')