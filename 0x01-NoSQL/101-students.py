#!/usr/bin/env python3
""" pymongo """


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """ get by average score """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
