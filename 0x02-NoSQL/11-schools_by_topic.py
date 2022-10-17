#!/usr/bin/env python3
"""returns the list of school having a specific topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns list of schools with certain topic"""
    topics = mongo_collection.find({"topics": topic})
    return topics
