from numpy import array

from thesaurus.word_vectors import query, word_vectors


def analogy(a, b, c):
    query_array = (
        array(word_vectors[b]) -
        array(word_vectors[a]) +
        array(word_vectors[c])
    )
    return query(query_array)


def addition(a, b):
    query_array = (
        array(word_vectors[b]) +
        array(word_vectors[a])
    )
    return query(query_array)


def subtraction(a, b):
    query_array = (
        array(word_vectors[a]) -
        array(word_vectors[b])
    )
    return query(query_array)


def nearest(word):
    query_array = array(word_vectors[word])
    return query(query_array)


def average(words):
    vectors = [array(word_vectors[word]) for word in words]
    print(vectors)
    return query(sum(vectors) / len(vectors))
