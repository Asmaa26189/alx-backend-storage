#!/usr/bin/env python3
""" pymongo """


def list_all(mongo_collection):
    """ get all """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
