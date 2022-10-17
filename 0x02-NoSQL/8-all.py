#!/usr/bin/env python3
"""lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all docuements in a collection"""
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
