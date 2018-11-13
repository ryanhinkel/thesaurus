from pyramid.view import view_config

from thesaurus import word_math


@view_config(
    route_name='addition',
    renderer='addition.html',
)
def addition(request):
    a = request.GET.get('a', 'food')
    b = request.GET.get('b', 'drink')
    error = None

    try:
        results = word_math.addition(a, b)
    except KeyError:
        results = []
        error = 'Some words were not found in the thesaurus'

    return {
        'a': a,
        'b': b,
        'results': results,
        'error': error,
    }
