import numpy

from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections

array = numpy.array

# Dimension of our vector space
dimension = 300

filename = 'glove.6B/glove.6B.{}d.small.txt'.format(dimension)
lines = open(filename).read().strip().split('\n')

word_vectors = {}
for line in lines:
    split_line = line.split()
    word = split_line[0]
    vec = [float(thing) for thing in split_line[1:]]
    word_vectors[word] = vec

# Create a random binary hash with 10 bits
rbp = RandomBinaryProjections('rbp', 2)

# Create engine with pipeline configuration
cosine = Engine(dimension, lshashes=[rbp])

for word, vec in word_vectors.items():
    cosine.store_vector(array(vec), word)

print('ready')


def query(array):
    return [res[1] for res in cosine.neighbours(array)]


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


def nearest(word):
    query_array = array(word_vectors[word])
    return query(query_array)
