#!/usr/bin/env python3
"""returns lsit of schools with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """refer to module doc"""
    return mongo_collection.find({"topics": topic})