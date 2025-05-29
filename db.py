from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["annotation_db"]

annotations_col = db["annotations"]
classes_col = db["classes"]
