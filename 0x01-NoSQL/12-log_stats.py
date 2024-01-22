#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    print(nginx.count_documents({}), "logs")

    methods = ["GET", "PUT", "POST", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count_method = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count_method}")

    print(nginx.count_documents({"method": "GET",
                                 "path": "/status"}), "status check")
