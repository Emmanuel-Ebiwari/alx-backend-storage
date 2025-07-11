#!/usr/bin/env python3
"""Module for a simple Redis-backed Cache class using redis-py."""

import redis
import uuid
from typing import Union, Optional, Callable

class Cache:
    """Cache class for storing and retrieving data from Redis."""

    def __init__(self) -> None:
        """Initialize the Cache instance with a clean Redis database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return the generated key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None) -> Union[str, int, float, bytes, None]:
        """
        Retrieve data from Redis by key, with optional conversion function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a UTF-8 decoded string from Redis.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer from Redis.
        """
        return self.get(key, fn=lambda d: int(d) if d else None)
