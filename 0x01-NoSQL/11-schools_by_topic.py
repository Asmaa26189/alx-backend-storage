#!/usr/bin/env python3
""" pymongo """


def schools_by_topic(mongo_collection, topic):
    """ get by """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
