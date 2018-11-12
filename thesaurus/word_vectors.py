import os

from numpy import array

from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections


try:
    dimensions = int(os.getenv('DIMENSIONS', 300))
except ValueError:
    print('couldnt parse dimensions, using 300')
    dimensions = 300

filename = os.getenv(
    'VECTORS_FILE', 'glove.6B/glove.6B.300d.small.txt')

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
nearest = Engine(dimensions, lshashes=[rbp])

for word, vec in word_vectors.items():
    nearest.store_vector(array(vec), word)

print('ready')


def query(array):
    return [res[1] for res in nearest.neighbours(array)]
