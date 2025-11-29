#!/usr/bin/env python3
"""salam"""


def insert_school(mongo_collection, **kwargs):
    """salam """
    d  = mongo_collection.insert_one(kwargs)
    return d.inserted_id
