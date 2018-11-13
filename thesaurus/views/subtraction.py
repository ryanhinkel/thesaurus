from pyramid.view import view_config

from thesaurus import word_math


@view_config(
    route_name='subtraction',
    renderer='subtraction.html',
)
def subtraction(request):
    a = request.GET.get('a', 'person')
    b = request.GET.get('b', 'brain')
    error = None

    try:
        results = word_math.subtraction(a, b)
    except KeyError:
        results = []
        error = 'Some words were not found in the thesaurus'

    return {
        'a': a,
        'b': b,
        'results': results,
        'error': error,
    }
