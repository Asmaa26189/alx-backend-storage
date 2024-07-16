#!/usr/bin/env python3
"""pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Insert new """
    return mongo_collection.insert(kwargs)
