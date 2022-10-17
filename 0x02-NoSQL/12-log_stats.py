#!/usr/bin/env python3
"""provides some stats about Nginx logs"""


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    logs = nginx_collection.find()
    g = 0
    sc = 0
    po = 0
    pu = 0
    pa = 0
    de = 0
    for l in logs:
        if g == 0:
        if l['method'] == 'GET':
            g += 1
            if l['path'] == '/status':
                sc += 1
        if l['method'] == 'POST':
            po += 1
        if l['method'] == 'PUT':
            pu += 1
        if l['method'] == 'PATCH':
            pa += 1
        if l['method'] == 'DELETE':
            de += 1

    print("Methods:")
    print("\tmethod GET: " + str(g))
    print("\tmethod POST: " + str(po))
    print("\tmethod PUT: " + str(pu))
    print("\tmethod PATCH: " + str(pa))
    print("\tmethod DELETE: " + str(de))
    print(str(sc) + " status check")
