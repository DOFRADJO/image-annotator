from fastapi import FastAPI, UploadFile, File
from annotation_service import (
    upload_images, annotate_image,
    get_classes, add_class, delete_class,
    get_annotations
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi import Body



app = FastAPI(title="Image Annotation Microservice")

class AnnotationPayload(BaseModel):
    image_name: str
    label: str
    user_id: str


@app.post("/annotate-db")
def annotate(payload: AnnotationPayload):
    print("🧠 Reçu pour annotation:", payload.dict())  # DEBUG ICI
    return annotate_image(payload.image_name, payload.label, payload.user_id)



@app.post("/classes")
def create_class(payload: dict = Body(...)):
    print("🔍 Reçu pour ajout de classe:", payload)  # DEBUG ICI
    label = payload.get("label")
    if not label:
        return {"status": "error", "message": "Aucun label fourni"}
    return add_class(label)

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

#@app.post("/annotate_db")
#def annotate(image_name: str, label: str, user_id: str):
 #   return annotate_image(image_name, label, user_id)

@app.get("/classes")
def list_classes():
    return get_classes()

@app.delete("/classes/{label}")
def remove_class(label: str):
    return delete_class(label)

@app.get("/annotations")
def list_annotations(format: str = "json"):
    return get_annotations(format)

@app.get("/export")
def export_annotations():
    return get_annotations("csv")