#!/usr/bin/env python3
"""Module for a simple Redis-backed Cache class using redis-py."""

import redis
import uuid
from typing import Union


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

    def get(self, key: str) -> Union[bytes, None]:
        """Get data from Redis by key"""
        return self._redis.get(key)
