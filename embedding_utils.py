import torch
from PIL import Image
import numpy as np

class DummyEmbedder:
    """Fallback embedder when dependencies aren't available"""
    def __init__(self):
        self.dim = 512  # CLIP-like dimension
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
    def get_text_embedding(self, text):
        return np.random.rand(1, self.dim).astype(np.float32)
    
    def get_image_embedding(self, image_path):
        return np.random.rand(1, self.dim).astype(np.float32)

try:
    from transformers import CLIPProcessor, CLIPModel
    
    class CLIPEmbedder:
        def __init__(self, model_name="openai/clip-vit-base-patch32"):
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.model = CLIPModel.from_pretrained(model_name).to(self.device)
            self.processor = CLIPProcessor.from_pretrained(model_name)
            self.dim = 512
            
        def get_text_embedding(self, text):
            inputs = self.processor(text=text, return_tensors="pt", padding=True, truncation=True).to(self.device)
            with torch.no_grad():
                text_features = self.model.get_text_features(**inputs)
            return text_features.cpu().numpy().astype(np.float32)
        
        def get_image_embedding(self, image_path):
            image = Image.open(image_path)
            inputs = self.processor(images=image, return_tensors="pt", padding=True).to(self.device)
            with torch.no_grad():
                image_features = self.model.get_image_features(**inputs)
            return image_features.cpu().numpy().astype(np.float32)
    
    Embedder = CLIPEmbedder  # Use real implementation if available
    
except ImportError:
    print("Warning: CLIP dependencies not found. Using dummy embedder.")
    Embedder = DummyEmbedder  # Fallback to dummy implementation
