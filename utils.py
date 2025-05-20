import os
from fastapi import UploadFile

async def save_files(files: list[UploadFile], folder: str):
    saved = []
    for file in files:
        file_path = os.path.join(folder, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        saved.append(file.filename)
    return saved
