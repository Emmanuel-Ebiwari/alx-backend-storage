import redis
import uuid

class Cache(object):
    def __init__(self):
        """Initialize the Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """Store data in Redis"""
        key = str(uuid.uuid4()) # Generate a random UUID (version 4)
        self._redis.set(key, data)
        return key

    def get(self, key):
        """Get data from Redis"""
        return self._redis.get(key)