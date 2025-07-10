# minigpt4-backend/app/utils.py
from PIL import Image
import io
import base64

def decode_base64_image(data: str) -> Image.Image:
    """Decode base64 string to PIL Image."""
    image_data = base64.b64decode(data)
    return Image.open(io.BytesIO(image_data)).convert("RGB")

def resize_image(image: Image.Image, max_size: int = 1024) -> Image.Image:
    """Resize image while maintaining aspect ratio."""
    w, h = image.size
    if max(w, h) > max_size:
        scale = max_size / max(w, h)
        return image.resize((int(w * scale), int(h * scale)))
    return image