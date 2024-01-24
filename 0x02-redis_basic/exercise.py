#!/usr/bin/env python3
"""script contain Cache class"""
import redis
from typing import Union, TypeVar
import uuid
T = TypeVar('T')


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """initialzion the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """storind data to redis and returning the key"""
        u_id = str(uuid.uuid4())
        self._redis.set(u_id, data)
        return u_id
