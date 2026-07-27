# Static Files & Media Storage Space (`static/`)

This directory serves as the storage location for user-uploaded files and static assets.

## Key Concept: Static Asset Serving (Django vs. FastAPI)
* **Django:** Static and media files are configured using `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL`, and `MEDIA_ROOT`. In production, you typically configure Nginx or WhiteNoise to serve these directories.
* **FastAPI:** You explicitly instantiate `StaticFiles` and mount it to your application instance.

## Understanding the Structure
* `uploads/`: Subdirectory reserved for user uploads. Keeps original file formats categorized and safely isolated.
* `.gitkeep`: Placeholder file to ensure Git tracks the folder even if it is empty.

## Mounting and Retrieving Files:
1. **Mounting:** Mounted inside [main.py](file:///home/jafor/Documents/fastapiandAI/app/main.py):
   ```python
   app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
   ```
2. **Accessing:** Any file stored inside `static/uploads/image.png` will be accessible publicly at the HTTP path `/static/uploads/image.png`.
