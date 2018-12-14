import os

from numpy import array

from thesaurus.config import filename
from thesaurus.engine import engine


WORD_VECTORS = {}

def load_vectors():
    print('loading vectors from {}'.format(filename))

    lines = open(filename).read().strip().split('\n')

    for line in lines:
        split_line = line.split()
        word = split_line[0]
        vec = array([float(thing) for thing in split_line[1:]])
        WORD_VECTORS[word] = vec

    print('loading vectors into engine')

    for word, vec in WORD_VECTORS.items():
        engine.store_vector(vec, word)


def get_word(word):
    return WORD_VECTORS[word]


if __name__ == '__main__':
    load_vectors()
