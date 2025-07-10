# minigpt4-backend/app/main.py
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from minigpt_wrapper import MiniGPT4Handler
from PIL import Image
from io import BytesIO
from utils import resize_image


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

minigpt = MiniGPT4Handler()

@app.post("/vision")
async def process_vision(
    image: UploadFile = File(...),
    prompt: str = Form("")
):
    contents = await image.read()
    img = Image.open(BytesIO(contents)).convert("RGB")
    img = resize_image(img, max_size=1024)
    response = minigpt.process_image(img, prompt)
    return {"response": response}
