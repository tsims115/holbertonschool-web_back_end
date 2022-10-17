#!/usr/bin/env python3
"""inserts insto school"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts kwargs into mongo_collection"""
    item = mongo_collection.insert_one(kwargs)
    return item.inserted_id
