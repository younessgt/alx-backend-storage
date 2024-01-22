#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    print(nginx.count_documents({}), "logs")
    
    count_get = nginx.count_documents({"method": "GET"})
    count_put = nginx.count_documents({"method": "PUT"})
    count_post = nginx.count_documents({"method": "POST"})
    count_patch = nginx.count_documents({"method": "PATCH"})
    count_delete = nginx.count_documents({"method": "DELETE"})

    print(f"""Methods:
            method GET: {count_get}
            method POST: {count_post}
            method PUT: {count_put}
            method PATCH: {count_patch}
            method DELETE: {count_delete}""")

    print(nginx.count_documents({"path": "/status"}), "status check")
