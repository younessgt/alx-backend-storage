#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    num_logs = nginx.count_documents({})
    print(f"{num_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count_method = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count_method}")

    num_status = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{num_status} status check")

    list_ip = nginx.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },

        {
            "$sort": {
                "count": -1
            }
        },
        {"$limit": 10}
    ])
    print("IPs:")
    for lis in list_ip:
        print(f"\t{lis.get('_id')}: {lis.get('count')}")
