#!/usr/bin/env python3
"""updates documents in collection"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """updates documents in collection"""
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
