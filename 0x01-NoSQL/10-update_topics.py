#!/usr/bin/env python3
""" script contain update_topics function"""


def update_topics(mongo_collection, name, topics):
    """ function that changes all topics
    of a school document based on the name"""

    criteria = {"name": name}
    topic = {"$set": {"topics": topics}}
    mongo_collection.update_many(criteria, topic)
