import chromadb
from chromadb.config import Settings
from embed import CLIPEmbedder
import os
from tqdm import tqdm

class ChromaIndexer:
    def __init__(self, persist_dir="chroma_db"):
        self.client = chromadb.PersistentClient(
            path=persist_dir,
            settings=Settings(allow_reset=True)
        )
        self.collection = self.client.get_or_create_collection(
            name="visual_search",
            metadata={"hnsw:space": "cosine"},
            embedding_function=None
        )
        self.embedder = CLIPEmbedder()
    
    def index_images(self, image_dir, batch_size=128):
        image_files = [
            os.path.join(image_dir, f) 
            for f in os.listdir(image_dir) 
            if f.endswith(('.jpg', '.jpeg', '.png'))
        ]
        
        for i in tqdm(range(0, len(image_files), batch_size), desc="Indexing"):
            batch_files = image_files[i:i+batch_size]
            embeddings = []
            metadatas = []
            ids = []
            
            for img_path in batch_files:
                embedding = self.embedder.embed_image(img_path)
                embeddings.append(embedding.tolist())
                metadatas.append({"path": img_path})
                ids.append(str(os.path.basename(img_path)))
            
            self.collection.upsert(
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
    
    def get_collection_stats(self):
        return self.collection.count()

def index_coco_dataset():
    indexer = ChromaIndexer()
    image_dir = "images/COCO_train2017"
    
    print("Indexing COCO images...")
    indexer.index_images(image_dir)
    print(f"Indexed {indexer.get_collection_stats()} images")

if __name__ == "__main__":
    index_coco_dataset()
