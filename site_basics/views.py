import conf
import datetime

from django.shortcuts import render_to_response
from django.contrib.sites.models import get_current_site
from django.template import RequestContext


def page_404(request):
    """
    Handler for 404 error page
    """
    response = render_to_response(conf.ERROR_404_PAGE_TEMPLATE, _get_content(request))
    response.status_code = 404
    return response


def page_500(request):
    """
    Handler for 500 error page
    """
    response = render_to_response(conf.ERROR_500_PAGE_TEMPLATE, _get_content(request))
    response.status_code = 500
    return response


def _get_content(request):
    site = get_current_site(request)
    nav_links = []
    if conf.ERROR_PAGE_CMS_LINKS:
        try:
            from menus.menu_pool import menu_pool
            from menus.templatetags.menu_tags import cut_levels
            from cms.models import Page
            try:
                for page in cut_levels(menu_pool.get_nodes(request, site_id=site.id), 0, 1, 0, 1000):
                    nav_links.append([
                        page.get_absolute_url(),
                        page.get_menu_title(),
                        ])
            except AttributeError: # if no user in request
                for page in Page.objects.on_site(site).public():
                    if page.is_root_node():
                        nav_links.append([
                            page.get_absolute_url(),
                            page.get_title(),
                        ])
        except ImportError:
            pass # django-cms is not installed

    if len(nav_links) == 0:
        nav_links = conf.ERROR_PAGE_NAV_LINKS
    return RequestContext(request, {
        'site': site,
        'year': datetime.datetime.now().year,
        'theme_name': conf.ERROR_PAGE_THEME,
        'theme_color': conf.ERROR_PAGE_THEME_COLOR,
        'theme_static_url': conf.ERROR_PAGE_THEME_STATIC_URL,
        'logo_url': conf.ERROR_PAGE_LOGO_URL,
        'nav_links': nav_links,
        'social_links': conf.ERROR_PAGE_SOCIAL_LINKS,
        'search_action': conf.ERROR_PAGE_SEARCH_ACTION,
        'search_method': conf.ERROR_PAGE_SEARCH_METHOD,
        'search_param': conf.ERROR_PAGE_SEARCH_PARAM,
    })
