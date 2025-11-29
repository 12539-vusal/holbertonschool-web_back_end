#!/usr/bin/env python3
"""salam"""


def schools_by_topic(mongo_collection, topic):
    """salam"""
    return mongo_collection.find({"topics": topic})
