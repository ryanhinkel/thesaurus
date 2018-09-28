import random

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest

from thesaurus import word_clustering

from codenames.words import words


@view_config(
    route_name='codewords',
    renderer='codewords.html',
)
def codewords(request):
    NUM_WORDS = 25

    random_words = random.sample(words, NUM_WORDS)
    spy_indexes = random.sample(range(NUM_WORDS), NUM_WORDS)

    assassin_index = spy_indexes[0]
    my_spies = spy_indexes[1:8]
    their_spies = spy_indexes[8:15]

    return {
        'words': random_words,
        'assassin': assassin_index,
        'my_spies': my_spies,
        'their_spies': their_spies,
    }


@view_config(route_name='clue', renderer='json')
def clue(request):
    good_words = [w.lower() for w in request.json_body['good_words']]
    bad_words = [w.lower() for w in request.json_body['bad_words']]

    if not good_words:
        return HTTPBadRequest('No good words')
    (word, number, allies, words) = word_clustering.get_suggestion(
        good_words, bad_words)
    return {'word': word, 'words': words, 'close_to': number, 'allies': allies}
