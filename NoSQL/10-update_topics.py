#!/usr/bin/env python3
"""update topic"""


def update_topics(mongo_collection, name, topics):
    """updates topic"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
