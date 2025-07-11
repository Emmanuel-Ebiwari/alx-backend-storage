#!/usr/bin/env python3
"""
Main file
"""
import redis
from exercise import replay

Cache = __import__('exercise').Cache

cache = Cache()

# Task 1
data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))


# Task 2
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    raw = local_redis.get(key)
    converted = cache.get(key, fn=fn)
    print("Raw from Redis:", raw)
    print("Converted via cache.get:", converted)
    assert converted == value

# Task 3
cache.store(b"first")
print(cache.get(cache.store.__qualname__))  # Should print b'1'

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))  # Should print b'3'

# Task 4
s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

# Task 5
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)