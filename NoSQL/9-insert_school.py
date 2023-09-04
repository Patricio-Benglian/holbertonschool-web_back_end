#!/usr/bin/env python3
"""insert into thing"""


def insert_school(mongo_collection, **kwargs):
    """inserts into collection"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.__id__
