#!/usr/bin/env python3
"""pymongo """


def insert_school(db, **kwargs):
    """ Insert new """
    return db.insert(kwargs)
