import os
import shutil
import uuid
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)

# Define target uploads directory
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "static", "uploads")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(..., description="The file payload to upload"),
    current_user: User = Depends(get_current_user)
):
    """
    Uploads a file to the static storage space.
    Enforces authentication: Only logged-in users can upload files.
    
    FastAPI File Upload Mechanics (For Django Developers):
    - In Django: You use `request.FILES['file']` which handles parsing multi-part form data via a UploadedFile subclass.
    - In FastAPI: Declaring `file: UploadFile = File(...)` automatically intercepts multi-part form data parser,
                 validates it, and yields an `UploadFile` instance.
    - UploadFile attributes:
      * `file`: A SpooledTemporaryFile (file-like object).
      * `filename`: The original string filename sent.
      * `content_type`: The content-type string (e.g. image/png).
    """
    # Ensure directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    # Sanitize and unique-ify file name to prevent collision
    # Using a UUID prefix ensures files with same name do not overwrite each other
    unique_prefix = uuid.uuid4().hex
    safe_filename = f"{unique_prefix}_{file.filename.replace(' ', '_')}"
    file_path = os.path.join(UPLOAD_DIR, safe_filename)
    
    try:
        # Save file to disk
        # We read chunk-by-chunk or copy the file object using shutil.copyfileobj
        # file.file is the underlying temporary file object
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Could not save file: {str(e)}"
        )
    finally:
        # Always close the file descriptor to free resources
        await file.close()
        
    # Get file size
    file_size = os.path.getsize(file_path)
    
    # Return structured metadata including the relative public static URL
    return {
        "filename": safe_filename,
        "content_type": file.content_type,
        "size": file_size,
        "url": f"/static/uploads/{safe_filename}"
    }
