#!/usr/bin/env python3
""" script contain list_all function"""


def list_all(mongo_collection):
    """  function that lists all documents in a collection """
    list_doc = [doc for doc in mongo_collection.find()]
    return list_doc
