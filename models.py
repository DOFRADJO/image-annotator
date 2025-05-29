from pydantic import BaseModel

class Annotation(BaseModel):
    image_name: str
    label: str
    user_id: str

class ClassLabel(BaseModel):
    label: str
