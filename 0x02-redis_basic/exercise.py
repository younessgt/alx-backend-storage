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


def call_history(method: Callable) -> Callable:
    """call_history decorator to store the history
    of inputs and outputs for a particular function"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""

        input_par = str(args)
        output = str(method(self, *args, **kwargs))

        key_input = key + ":inputs"
        key_output = key + ":outputs"

        self._redis.rpush(key_input, input_par)
        self._redis.rpush(key_output, output)

        return output

    return wrapper


def replay(method: Callable):
    """function to display the history of calls of a particular function """
    r = redis.Redis()
    inputs = r.lrange("{}:inputs".format(method.__qualname__),
                      0, -1)
    outputs = r.lrange("{}:outputs".format(method.__qualname__),
                       0, -1)

    paired_obj = zip(inputs, outputs)

    paired_converted_list = [(key.decode("utf-8"), value.decode("utf-8"))
                             for key, value in paired_obj]

    list_length = len(paired_converted_list)
    print(f"{method.__qualname__} was called {list_length} times:")

    for key, value in paired_converted_list:
        print(f"{method.__qualname__}(*{key}) -> {value}")


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """initialzion the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
