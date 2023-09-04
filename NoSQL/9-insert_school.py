#!/usr/bin/env python3
"""insert into thing"""
from pymongo import InsertOne


def insert_school(mongo_collection, **kwargs):
    """inserts into collection"""
    new_doc = mongo_collection.InsertOne(kwargs)
    return new_doc.__id__
