#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")

"""if we dont use wraps(method) on the exercice script 
cache.store.__qualname__ we return the name and doc of the wrapper
function and not the store method"""
print(cache.get(cache.store.__qualname__))

print(cache.store.__qualname__)
cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
