from pyramid.view import view_config

import thesaurus


@view_config(
    route_name='nearest',
    renderer='nearest.html',
)
def nearest(request):
    word = request.GET.get('word')
    error = None

    try:
        results = thesaurus.nearest(word)
    except KeyError:
        word = 'nothing'
        results = []
        error = 'The word was not found in the thesaurus'

    return {
        'word': word,
        'results': results,
        'error': error,
    }
