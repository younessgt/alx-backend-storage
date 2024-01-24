#!/usr/bin/env python3
"""script contain Cache class"""
import redis
from typing import Optional, Union, Callable, Any
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counting how many times the method
    has been called"""
    key = method.__qualname__

    """ we used wraps(method) to keep the original function’s name
    docstring, etc ... see main2.py"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ method that perfom the incrementation"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """initialzion the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """storind data to redis and returning the key"""
        u_id = str(uuid.uuid4())
        self._redis.set(u_id, data)
        return u_id

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Any:
        """ method to retrieve the data from redis and converted
        to a desired type """

        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """method to retrieve a data and convert it to str"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ method to retrieve data and convert it to int"""
        value = self._redis.get(key)
        try:
            value_conv = int(value.decode("utf-8"))
        except Exception:
            value_conv = 0
        return value_conv
