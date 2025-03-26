import torch
import clip
from PIL import Image
import numpy as np
import warnings

class CLIPEmbedder:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = self._load_model()
        self.embedding_dim = 512
        
    def _load_model(self):
        try:
            model, preprocess = clip.load("ViT-B/32", device=self.device)
            print(f"CLIP model loaded on {self.device}")
            return model, preprocess
        except Exception as e:
            warnings.warn(f"Failed to load CLIP model: {e}. Using random embeddings.")
            return None, None
    
    def embed_text(self, text):
        if self.model is None:
            return np.random.rand(self.embedding_dim).astype(np.float32)
        
        with torch.no_grad():
            text_input = clip.tokenize([text]).to(self.device)
            text_features = self.model.encode_text(text_input)
            return text_features.cpu().numpy().astype(np.float32)[0]
    
    def embed_image(self, image_path):
        if self.model is None:
            return np.random.rand(self.embedding_dim).astype(np.float32)
        
        try:
            image = Image.open(image_path)
            image = self.preprocess(image).unsqueeze(0).to(self.device)
            with torch.no_grad():
                image_features = self.model.encode_image(image)
                return image_features.cpu().numpy().astype(np.float32)[0]
        except Exception as e:
            warnings.warn(f"Error processing image {image_path}: {e}")
            return np.random.rand(self.embedding_dim).astype(np.float32)
