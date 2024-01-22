#!/usr/bin/env python3
""" script contain insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """ function that inserts a new document
    in a collection based on kwargs """
    obj = {}
    for key, value in kwargs.items():
        obj[key] = value
    mongo_collection.insert_one(obj)
    for objec in mongo_collection.find(obj):
        return objec.get('_id')
