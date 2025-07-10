# minigpt4-backend/app/minigpt_wrapper.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from torchvision import transforms
from PIL import Image
import torch

class MiniGPT4Handler:
    def _init_(self):
        print("Loading MiniGPT-4 (BLIP placeholder)...")
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model.eval()

    def process_image(self, image: Image.Image, prompt: str = "") -> str:
        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            out = self.model.generate(**inputs)
        result = self.processor.decode(out[0], skip_special_tokens=True)
        return result
