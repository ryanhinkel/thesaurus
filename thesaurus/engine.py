import numpy
import pickle

from redis import Redis
from nearpy import Engine
from nearpy.distances import ManhattanDistance
from nearpy.filters import NearestFilter
from nearpy.hashes import RandomBinaryProjections
from nearpy.storage.storage_redis import RedisStorage

from thesaurus.config import dimensions, REDIS_HOST, REDIS_PORT, REDIS_DB


class CustomRedisStorage(RedisStorage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _format_word_key(self, word):
        return 'words:{}'.format(word)

    def store_vector(self, hash_name, bucket_key, v, data):
        super().store_vector(hash_name, bucket_key, v, data)
        key = self._format_word_key(data)
        val_dict = {
            'vector': v.tostring(),
            'dtype': v.dtype.name
        }
        self.redis_object.set(key, pickle.dumps(val_dict, protocol=2))

    def get_word(self, word):
        value = self.redis_object.get(self._format_word_key(word))
        if value:
            val_dict = pickle.loads(value)
            return numpy.fromstring(val_dict['vector'], dtype=val_dict['dtype'])
        raise ValueError('{} not found!'.format(word))


# Create redis storage adapter
redis_object = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
redis_storage = CustomRedisStorage(redis_object)

# Get hash config from redis
config = redis_storage.load_hash_configuration('thesaurus')

if config is None:
    # Config is not existing, create hash from scratch
    lshash = RandomBinaryProjections('rbp', 2, rand_seed=42)
    redis_storage.store_hash_configuration(lshash)
else:
    # Config is existing, create hash with None parameters
    lshash = RandomBinaryProjections(None, None)
    # Apply configuration loaded from redis
    lshash.apply_config(config)


engine = Engine(
    dimensions,
    distance=ManhattanDistance(),
    vector_filters=[NearestFilter(20)],
    lshashes=[lshash],
    storage=redis_storage,
)


def query(array):
    return [res[1] for res in engine.neighbours(array)]
