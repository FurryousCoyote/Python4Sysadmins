#!/usr/bin/python3

from pymongo import MongoClient


client = MongoClient()
db = client['flask-app']

print(db.usuarios.find())
