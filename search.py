import chromadb
from chromadb.config import Settings
from embed import CLIPEmbedder
import time

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
    
    def search_by_text(self, query, k=3):  # Changed default k to 3
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
    
    def search_by_image(self, image_path, k=3):  # Changed default k to 3
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

def print_menu():
    print("\nMenu Options:")
    print("1. Vision language search")
    print("2. Change the value of k (current: {})".format(k_value))
    print("3. Exit")

if __name__ == "__main__":
    searcher = VisualSearcher()
    k_value = 3  # Default value
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            query = input("Enter text query: ")
            if query.lower() == 'exit':
                break
                
            if query.endswith(('.jpg', '.jpeg', '.png')):
                results, latency = searcher.search_by_image(query, k_value)
                print(f"Image search results for {query}:")
            else:
                results, latency = searcher.search_by_text(query, k_value)
                print(f"Text search results for '{query}':")
            
            for i, (path, score) in enumerate(results, 1):
                print(f"{i}. {path} (score: {score:.3f})")
            print(f"Latency: {latency:.1f}ms")
            
        elif choice == "2":
            try:
                new_k = int(input("Enter new value for k: "))
                if new_k > 0:
                    k_value = new_k
                    print(f"k value changed to {k_value}")
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
        elif choice == "3":
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
