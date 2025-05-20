# Image Annotation Microservice

This microservice allows uploading images, assigning labels to them, and managing annotation classes.

## Endpoints

- `POST /upload`: Upload images
- `POST /annotate`: Annotate an image
- `GET /classes`: List available classes
- `POST /classes`: Add a class
- `DELETE /classes/{label}`: Delete a class
- `GET /annotations`: Get annotations (JSON or CSV)

## Requirements

- Python 3.9+
- MongoDB running on localhost:27017

## Running the service

```bash
uvicorn main:app --reload
