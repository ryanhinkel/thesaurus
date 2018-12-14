import os

from wsgiref.simple_server import make_server
from pyramid.config import Configurator


environment = os.getenv('ENV')
try:
    dimensions = int(os.getenv('DIMENSIONS', 300))
except ValueError:
    print('couldnt parse dimensions, using 300')
    dimensions = 300
filename = os.getenv('VECTORS_FILE', 'glove.6B/glove.6B.300d.small.txt')

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)


def configure():
    settings = {}
    if environment == 'development':
        settings.setdefault("pyramid.reload_assets", True)
        settings.setdefault("pyramid.reload_templates", True)

    with Configurator(settings=settings) as config:
        if environment == 'development':
            config.include('pyramid_debugtoolbar')

        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.html')
        config.add_jinja2_search_path("thesaurus:templates", name=".html")

        # Thesaurus
        config.add_route('nearest', '/')
        config.add_route('analogy', '/analogy')
        config.add_route('addition', '/addition')
        config.add_route('average', '/average')
        config.add_route('subtraction', '/subtraction')

        # Codenames
        config.add_route('codewords', '/codewords')
        config.add_route('clue', '/clue')

        # Serve our static files
        prevent_http_cache = config.get_settings().get(
            "pyramid.prevent_http_cache", False
        )
        config.add_static_view(
            "static",
            "thesaurus:static/",
            cache_max_age=0 if prevent_http_cache else 10 * 365 * 24 * 60 * 60,
        )

        config.scan('thesaurus.views')

    return config

