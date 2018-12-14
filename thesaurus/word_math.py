from numpy import array

from thesaurus.engine import query
from thesaurus.word_vectors import get_word


def analogy(a, b, c):
    query_array = (
        array(get_word(b)) -
        array(get_word(a)) +
        array(get_word(c))
    )
    return query(query_array)


def addition(a, b):
    query_array = (
        array(get_word(b)) +
        array(get_word(a))
    )
    return query(query_array)


def subtraction(a, b):
    query_array = (
        array(get_word(a)) -
        array(get_word(b))
    )
    return query(query_array)


def average(words):
    vectors = [array(get_word(word)) for word in words]
    return query(sum(vectors) / len(vectors))


def nearest(word):
    query_array = array(get_word(word))
    return query(query_array)
