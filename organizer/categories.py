# _ represents internal data (readability)
_EXTENSION_MAP = {
    # Documents
    "pdf": "Documents", "docx": "Documents", "doc": "Documents",
    "txt": "Documents", "xlsx": "Documents", "xls": "Documents",
    "pptx": "Documents", "ppt": "Documents", "csv": "Documents",
    
    # Images
    "jpg": "Images", "jpeg": "Images", "png": "Images",
    "gif": "Images", "bmp": "Images", "tiff": "Images",
    "webp": "Images", "svg": "Images", "cr2": "Images",
    
    # Videos
    "mp4": "Videos", "mov": "Videos", "avi": "Videos",
    "mkv": "Videos", "wmv": "Videos", "flv": "Videos", "webm": "Videos",
    
    # Audio
    "mp3": "Audio", "wav": "Audio", "flac": "Audio",
    "aac": "Audio", "ogg": "Audio", "wma": "Audio",
    
    # Archives
    "zip": "Archives", "rar": "Archives", "7z": "Archives",
    "tar": "Archives", "gz": "Archives", "bz2": "Archives", "xz": "Archives",
    
    # Code
    "py": "Code", "js": "Code", "html": "Code", "css": "Code",
    "java": "Code", "cpp": "Code", "c": "Code", "cs": "Code",
    "go": "Code", "rs": "Code", "rb": "Code", "php": "Code", "sh": "Code",
}


def get_category(filename: str) -> str:
    """
        Return category for a filename based on its extension.
    
        Args:
            filename: e.g., "report.PDF", "photo.JPEG", "archive.tar.gz"
        
        Returns:
        Category name (e.g., "Documents") or "Others" if unknown.
    """
    
    parts = filename.split(".")
    if len(parts) <= 1:
        return "Others"

    ext = parts[-1].lower()

    return _EXTENSION_MAP.get(ext,"Others")
        
    
    
