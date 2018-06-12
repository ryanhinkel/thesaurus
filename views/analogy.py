from pyramid.view import view_config

import thesaurus


@view_config(
    route_name='analogy',
    renderer='analogy.html',
)
def analogy(request):
    c = request.GET.get('c')
    a = request.GET.get('a')
    b = request.GET.get('b')
    error = None

    try:
        results = thesaurus.analogy(a, b, c)
    except KeyError:
        a = 'nothing'
        b = 'something'
        c = 'everything'
        results = []
        error = 'The word was not found in the thesaurus'

    return {
        'a': a,
        'b': b,
        'c': c,
        'results': results,
        'error': error,
    }
