import os

from numpy import array

from thesaurus.config import filename
from thesaurus.engine import engine


print('loading vectors from {}'.format(filename))

lines = open(filename).read().strip().split('\n')

word_vectors = {}
for line in lines:
    split_line = line.split()
    word = split_line[0]
    vec = array([float(thing) for thing in split_line[1:]])
    word_vectors[word] = vec

print('loading vectors into engine')

for word, vec in word_vectors.items():
    engine.store_vector(vec, word)

print('ready')
