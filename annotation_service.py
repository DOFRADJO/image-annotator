import os
from db import annotations_col, classes_col
from datetime import datetime
from utils import save_files

UPLOAD_FOLDER = "uploads"

async def upload_images(files):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    saved = await save_files(files, UPLOAD_FOLDER)
    return {"uploaded": saved}

def annotate_image(image_name, label, user_id):
    data = {
        "image_name": image_name,
        "label": label,
        "user_id": user_id,
        "upload_date": datetime.utcnow()
    }
    annotations_col.update_one(
        {"image_name": image_name},
        {"$set": data},
        upsert=True
    )
    return {"status": "success", "annotation": data}

def get_classes():
    return list(classes_col.find({}, {"_id": 0}))

def add_class(label):
    if classes_col.find_one({"label": label}):
        return {"error": "Class already exists"}
    classes_col.insert_one({"label": label})
    return {"added": label}

def delete_class(label):
    classes_col.delete_one({"label": label})
    return {"deleted": label}

def get_annotations(format="json"):
    cursor = annotations_col.find({}, {"_id": 0})
    data = list(cursor)
    if format == "csv":
        lines = ["image_name,label"]
        lines += [f"{d['image_name']},{d['label']}" for d in data]
        return {"format": "csv", "content": "\n".join(lines)}
    return {"format": "json", "content": data}
