import os

from numpy import array

from thesaurus.config import filename
from thesaurus.engine import engine


def load_vectors():
    print('loading vectors from {}'.format(filename))

    lines = open(filename).read().strip().split('\n')

    for line in lines:
        split_line = line.split()
        word = split_line[0]
        vec = array([float(thing) for thing in split_line[1:]])
        engine.store_vector(vec, word)


def get_word(word):
    return engine.storage.get_word(word)


if __name__ == '__main__':
    load_vectors()
