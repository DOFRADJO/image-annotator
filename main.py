from fastapi import FastAPI, UploadFile, File
from annotation_service import (
    upload_images, annotate_image,
    get_classes, add_class, delete_class,
    get_annotations
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles



app = FastAPI(title="Image Annotation Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en prod remplace par ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    return await upload_images(files)

@app.post("/annotate")
def annotate(image_name: str, label: str, user_id: str):
    return annotate_image(image_name, label, user_id)

@app.get("/classes")
def list_classes():
    return get_classes()

@app.post("/classes")
def create_class(label: str):
    return add_class(label)

@app.delete("/classes/{label}")
def remove_class(label: str):
    return delete_class(label)

@app.get("/annotations")
def list_annotations(format: str = "json"):
    return get_annotations(format)
