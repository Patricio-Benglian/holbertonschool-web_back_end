#!/usr/bin/env python3
"""module hahah ah ahah ah aha"""
import pymongo


def list_all(mongo_collection):
    """lists all in collection"""
    output = mongo_collection.find()
    return output
