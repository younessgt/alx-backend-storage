#!/usr/bin/env python3
""" srcipt contain top_students function"""


def top_students(mongo_collection):
    """ function that returns all students sorted by average score """
    list_topic = []
    for student in mongo_collection.find():
        topics = student.get("topics", [])
        average_s = 0
        if topics:
            sum_score = sum(float(topic.get("score", 0)) for topic in topics)
            average_s = sum_score / len(topics)
        mongo_collection.update_one({"_id": student["_id"]},
                                    {"$set": {"averageScore": average_s}})
    return list(mongo_collection.find().sort("id", -1))
