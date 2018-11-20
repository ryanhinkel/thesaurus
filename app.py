import os

from wsgiref.simple_server import make_server
from pyramid.config import Configurator

# does this work? YEEESSSSSS
settings = {
    'pyramid.reload_assets': True,
    'pyramid.reload_templates': True,
}

with Configurator(settings=settings) as config:
    if os.getenv('ENV') == 'development':
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
    app = config.make_wsgi_app()


if __name__ == '__main__':
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
