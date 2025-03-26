import os
import pickle
import numpy as np
from tqdm import tqdm
from embedding_utils import Embedder

class VisualSearchIndex:
    def __init__(self, image_dir, annotation_file):
        self.image_dir = image_dir
        self.annotation_file = annotation_file
        self.embedder = Embedder()  # Uses real or dummy embedder
        self.index = None
        self.image_paths = []
        
    def build_index(self):
        """Build index with fallback to dummy data if FAISS unavailable"""
        from pycocotools.coco import COCO
        coco = COCO(self.annotation_file)
        
        # Get image paths
        img_ids = coco.getImgIds()
        self.image_paths = [
            os.path.join(self.image_dir, f"COCO_train2017_{str(img_id).zfill(12)}.jpg") 
            for img_id in img_ids
        ]
        
        # Create index (FAISS or fallback)
        try:
            import faiss
            self.index = faiss.IndexFlatIP(self.embedder.dim)
            print("Using FAISS for vector search")
        except ImportError:
            self.index = None
            print("Warning: FAISS not available. Using linear search fallback.")
        
        # Generate embeddings
        embeddings = []
        for img_path in tqdm(self.image_paths, desc="Indexing images"):
            embeddings.append(self.embedder.get_image_embedding(img_path))
        
        self.embeddings = np.vstack(embeddings)
        
        if self.index is not None:
            self.index.add(self.embeddings)
            
    def save_index(self, index_path="index.pkl"):
        """Save index data using pickle fallback"""
        with open(index_path, "wb") as f:
            pickle.dump({
                'embeddings': self.embeddings,
                'image_paths': self.image_paths,
                'use_faiss': self.index is not None
            }, f)
            
    def load_index(self, index_path="index.pkl"):
        """Load index data with format detection"""
        with open(index_path, "rb") as f:
            data = pickle.load(f)
            self.embeddings = data['embeddings']
            self.image_paths = data['image_paths']
            
            if data.get('use_faiss', False):
                try:
                    import faiss
                    self.index = faiss.IndexFlatIP(self.embeddings.shape[1])
                    self.index.add(self.embeddings)
                except ImportError:
                    self.index = None
                    print("Warning: FAISS unavailable during load. Using linear search.")
            else:
                self.index = None
