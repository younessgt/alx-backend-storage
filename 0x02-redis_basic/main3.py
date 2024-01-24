#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
print(inputs)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

paired_keys_values = zip(inputs, outputs)

print(paired_keys_values)

paired_keys_values = [(key.decode("utf-8"), value.decode("utf_8")) for key, value in paired_keys_values]
print(paired_keys_values)
