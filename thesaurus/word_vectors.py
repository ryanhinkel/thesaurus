import os

from numpy import array

from thesaurus.config import filename
from thesaurus.engine import engine


def load_vectors(debug=False):
    if debug:
        print('loading vectors from {}'.format(filename))

    lines = open(filename).read().strip().split('\n')

    for i, line in enumerate(lines):
        if debug and i % 1_000 == 0:
            print('done {} / {} ({}%)'.format(i, len(lines), 100.0 * float(i)/len(lines)))

        split_line = line.split()
        word = split_line[0]
        try:
            engine.storage.get_word(word)
        except ValueError:
            vec = array([float(thing) for thing in split_line[1:]])
            engine.store_vector(vec, word)


def get_word(word):
    return engine.storage.get_word(word)


if __name__ == '__main__':
    load_vectors(debug=True)
