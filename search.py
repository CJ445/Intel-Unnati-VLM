import chromadb
from chromadb.config import Settings
from embed import CLIPEmbedder
import time
import argparse

class VisualSearcher:
    def __init__(self, persist_dir="chroma_db"):
        self.client = chromadb.PersistentClient(
            path=persist_dir,
            settings=Settings()
        )
        self.collection = self.client.get_collection(
            name="visual_search",
            embedding_function=None
        )
        self.embedder = CLIPEmbedder()
    
    def search_by_text(self, query, k=5):
        start_time = time.time()
        query_embedding = self.embedder.embed_text(query)
        
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k,
            include=["metadatas", "distances"]
        )
        
        latency_ms = (time.time() - start_time) * 1000
        formatted_results = [
            (item["path"], 1 - distance)
            for item, distance in zip(results["metadatas"][0], results["distances"][0])
        ]
        return formatted_results, latency_ms
    
    def search_by_image(self, image_path, k=5):
        start_time = time.time()
        query_embedding = self.embedder.embed_image(image_path)
        
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k,
            include=["metadatas", "distances"]
        )
        
        latency_ms = (time.time() - start_time) * 1000
        formatted_results = [
            (item["path"], 1 - distance)
            for item, distance in zip(results["metadatas"][0], results["distances"][0])
        ]
        return formatted_results, latency_ms

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Text query or image path")
    parser.add_argument("--k", type=int, default=5, help="Number of results")
    args = parser.parse_args()
    
    searcher = VisualSearcher()
    
    if args.query.endswith(('.jpg', '.jpeg', '.png')):
        results, latency = searcher.search_by_image(args.query, args.k)
        print(f"Image search results for {args.query}:")
    else:
        results, latency = searcher.search_by_text(args.query, args.k)
        print(f"Text search results for '{args.query}':")
    
    for i, (path, score) in enumerate(results, 1):
        print(f"{i}. {path} (score: {score:.3f})")
    print(f"Latency: {latency:.1f}ms")
