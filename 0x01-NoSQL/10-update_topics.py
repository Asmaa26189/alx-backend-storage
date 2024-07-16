#!/usr/bin/env python3
""" pymongo """


def update_topics(mongo_collection, name, topics):
    """ update """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
