#!/usr/bin/env python3
""" script contain schools_by_topic function"""


def schools_by_topic(mongo_collection, topic):
    """  function that returns the list of
    school having a specific topic"""
    topic = {"topics": topic}
    return [doc for doc in mongo_collection.find(topic)]
