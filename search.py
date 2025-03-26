import numpy as np
from typing import List, Tuple

class VisualSearcher:
    def __init__(self, index_path: str = "index.pkl"):
        """
        Initialize with either FAISS or fallback linear search
        """
        self.load_index(index_path)
        
    def load_index(self, index_path: str):
        """
        Load pre-built index with automatic backend detection
        """
        import pickle
        with open(index_path, "rb") as f:
            data = pickle.load(f)
            self.embeddings = data['embeddings']
            self.image_paths = data['image_paths']
            self.use_faiss = data.get('use_faiss', False)
            
            if self.use_faiss:
                try:
                    import faiss
                    self.index = faiss.IndexFlatIP(self.embeddings.shape[1])
                    self.index.add(self.embeddings)
                except ImportError:
                    self.use_faiss = False
                    print("FAISS not available - falling back to linear search")

    def _cosine_similarity(self, query_vec: np.ndarray, k: int) -> List[Tuple[str, float]]:
        """
        Fallback linear search using cosine similarity
        """
        # Normalize vectors
        query_norm = query_vec / np.linalg.norm(query_vec)
        embeddings_norm = self.embeddings / np.linalg.norm(self.embeddings, axis=1, keepdims=True)
        
        # Compute similarities
        similarities = np.dot(embeddings_norm, query_norm.T).flatten()
        
        # Get top-k results
        top_indices = np.argpartition(similarities, -k)[-k:]
        top_indices = top_indices[np.argsort(similarities[top_indices])[::-1]]
        
        return [(self.image_paths[i], float(similarities[i])) for i in top_indices]

    def search_by_vector(self, query_vec: np.ndarray, k: int = 10) -> List[Tuple[str, float]]:
        """
        Unified search interface for both FAISS and linear search
        """
        query_vec = query_vec.astype(np.float32)
        
        if self.use_faiss:
            distances, indices = self.index.search(query_vec, k)
            return [(self.image_paths[i], float(distances[0][j])) 
                    for j, i in enumerate(indices[0])]
        else:
            return self._cosine_similarity(query_vec, k)

    def search_by_text(self, text: str, k: int = 10) -> List[Tuple[str, float]]:
        """Search using text query"""
        from embedding_utils import Embedder
        query_vec = Embedder().get_text_embedding(text)
        return self.search_by_vector(query_vec, k)

    def search_by_image(self, image_path: str, k: int = 10) -> List[Tuple[str, float]]:
        """Search using image query""" 
        from embedding_utils import Embedder
        query_vec = Embedder().get_image_embedding(image_path)
        return self.search_by_vector(query_vec, k)
