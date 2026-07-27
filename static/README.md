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

---

## Detailed Code Walkthrough

### 1. Mounting Static Files
In [main.py](file:///home/jafor/Documents/fastapiandAI/app/main.py):
```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
```
* **`"/static"`**: The URL path prefix. Any incoming HTTP request starting with `/static` (e.g., `GET /static/uploads/example.txt`) is automatically matched.
* **`StaticFiles(directory=STATIC_DIR)`**: Instantiates the static asset serving service, bound to the physical absolute path of the `static` folder on disk. It reads the local file, infers the MIME type (e.g. `text/css`, `image/png`), sets HTTP headers (like `Content-Length`), and returns the file stream.
* **`name="static"`**: Internal identifier name, allowing you to generate static links inside templates (using `request.url_for("static", path="...")`), similar to Django's `{% static 'path' %}` template tag.

---

## How to Retrieve serving files (Step-by-Step)

Once files are stored in `static/uploads/`, retrieving them is straightforward:

1. **Verify the file exists on disk:**
   Check the folder inside your workspace: `/home/jafor/Documents/fastapiandAI/static/uploads/`.
   
2. **Access it via HTTP:**
   Open a browser tab or send a `curl` request:
   ```bash
   curl -i "http://127.0.0.1:8000/static/uploads/449b10fc206d475880efd77b528345b4_demo_file.txt"
   ```
   * The server returns:
     ```text
     HTTP/1.1 200 OK
     content-type: text/plain; charset=utf-8
     content-length: 33
     
     FastAPI file upload content data.
     ```

