from numpy import array, linalg

from thesaurus.word_vectors import get_word
from thesaurus.word_math import average


def delta(word1, word2):
    '''
    This function returns the distance between two vectors
    '''
    return linalg.norm(
        array(get_word(word1)) -
        array(get_word(word2))
    )


def compute_distances(target, list_of_words):
    '''
    This function calculates the distance from the target for each word
    and returns the distances in a dictionary.
    '''
    distances = {}
    for word in list_of_words:
        distances[word] = delta(target, word)
    return distances


def compute_closest_good_words(target, bad_words, good_words):
    '''
    This function takes a target and a list of good words and bad words.
    It returns a list of good words that are closer than the nearest bad word.
    '''
    max_distance = 10

    closest_bad_word = 10000000
    for word in bad_words:
        distance = delta(target, word)
        if distance < closest_bad_word:
            closest_bad_word = distance

    close_good_words = []
    for word in good_words:
        distance = delta(target, word)
        if distance < closest_bad_word and distance < max_distance:
            close_good_words.append(word)

    return close_good_words


def find_best_cluster(good_words, bad_words):
    '''
    This function finds the word with the highest number of close good words
    and returns that word and the close good words as a tuple
    '''
    best_word = None
    close_good_words = []
    for word in good_words:
        allies = compute_closest_good_words(word, bad_words, good_words)
        if (len(allies) > len(close_good_words)):
            best_word = word
            close_good_words = allies

    return (best_word, close_good_words)


def filter_legal_words(avoid_words):
    def f(clue):
        for word in avoid_words:
            if (clue == word or clue in word or word in clue):
                return False
        return True

    return f


def get_suggestion(good_words, bad_words):
    legal_words = filter_legal_words(good_words)
    (best_word, close_good_words) = find_best_cluster(good_words, bad_words)
    results = average(close_good_words)
    best = [word for word in filter(legal_words, results)]
    return (best[0], len(close_good_words), close_good_words, best)
