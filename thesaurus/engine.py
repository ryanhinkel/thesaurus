from nearpy import Engine
from nearpy.distances import ManhattanDistance
from nearpy.filters import NearestFilter
from nearpy.hashes import RandomBinaryProjections

from thesaurus.config import dimensions


engine = Engine(
    dimensions,
    distance=ManhattanDistance(),
    vector_filters=[NearestFilter(20)],
    lshashes=[RandomBinaryProjections('rbp', 2, rand_seed=42)]
)

def query(array):
    return [res[1] for res in engine.neighbours(array)]
