from pyramid.view import view_config

from thesaurus import word_math


@view_config(
    route_name='average',
    renderer='average.html',
)
def average(request):
    a = request.GET.get('a', 'red')
    b = request.GET.get('b', 'blue')
    error = None

    try:
        results = word_math.average([a, b])
    except KeyError:
        results = []
        error = 'Some words were not found in the thesaurus'

    return {
        'a': a,
        'b': b,
        'results': results,
        'error': error,
    }
