import os

from numpy import array

from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
from nearpy.distances import ManhattanDistance
from nearpy.filters import NearestFilter


try:
    dimensions = int(os.getenv('DIMENSIONS', 300))
except ValueError:
    print('couldnt parse dimensions, using 300')
    dimensions = 300

filename = os.getenv(
    'VECTORS_FILE', 'glove.6B/glove.6B.300d.small.txt')

print('loading vectors')

lines = open(filename).read().strip().split('\n')

word_vectors = {}
for line in lines:
    split_line = line.split()
    word = split_line[0]
    vec = array([float(thing) for thing in split_line[1:]])
    word_vectors[word] = vec

print('starting engine')

nearest = Engine(
    dimensions,
    distance=ManhattanDistance(),
    vector_filters=[NearestFilter(20)],
    lshashes=[RandomBinaryProjections('rbp', 2)]
)

for word, vec in word_vectors.items():
    nearest.store_vector(vec, word)

print('ready')


def query(array):
    return [res[1] for res in nearest.neighbours(array)]
