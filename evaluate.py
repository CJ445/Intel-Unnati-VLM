import json
import numpy as np
from typing import Dict, List
from search import VisualSearcher
from pycocotools.coco import COCO

class SearchEvaluator:
    def __init__(self, searcher: VisualSearcher, annotation_file: str):
        self.searcher = searcher
        self.coco = COCO(annotation_file)
        self.img_ids = self.coco.getImgIds()
        
    def _get_ground_truth(self, query: str, top_k: int = 50) -> List[int]:
        """Get relevant image IDs for a text query using COCO captions"""
        ann_ids = self.coco.getAnnIds(imgIds=self.img_ids)
        annotations = self.coco.loadAnns(ann_ids)
        
        relevant = []
        for ann in annotations:
            if query.lower() in ann['caption'].lower():
                if ann['image_id'] not in relevant:
                    relevant.append(ann['image_id'])
                    if len(relevant) >= top_k:
                        break
        return relevant
    
    def precision_at_k(self, query: str, k_values: List[int] = [1, 5, 10]) -> Dict[int, float]:
        """Calculate precision@k for different k values"""
        relevant = self._get_ground_truth(query)
        if not relevant:
            return {k: 0.0 for k in k_values}
            
        results = self.searcher.search_by_text(query, max(k_values))
        result_ids = [int(p.split('_')[-1].split('.')[0]) for p, _ in results]
        
        metrics = {}
        for k in k_values:
            top_k = result_ids[:k]
            relevant_found = len([i for i in top_k if i in relevant])
            metrics[k] = relevant_found / k
        return metrics
    
    def mean_average_precision(self, queries: List[str], k: int = 10) -> float:
        """Calculate MAP@k across multiple test queries"""
        aps = []
        for query in queries:
            relevant = self._get_ground_truth(query)
            if not relevant:
                continue
                
            results = self.searcher.search_by_text(query, k)
            result_ids = [int(p.split('_')[-1].split('.')[0]) for p, _ in results]
            
            precision_values = []
            relevant_count = 0
            for i, img_id in enumerate(result_ids, 1):
                if img_id in relevant:
                    relevant_count += 1
                    precision_values.append(relevant_count / i)
            
            ap = sum(precision_values) / len(relevant) if precision_values else 0
            aps.append(ap)
            
        return sum(aps) / len(queries) if aps else 0

    def evaluate_queries(self, test_queries: List[str]) -> Dict:
        """Comprehensive evaluation for multiple metrics"""
        return {
            "MAP@10": self.mean_average_precision(test_queries),
            "Precision@K": {query: self.precision_at_k(query) for query in test_queries}
        }

# Example Test Queries (expand with your own)
TEST_QUERIES = [
    "dog",
    "person riding a bike", 
    "car on the street",
    "table with food"
]

def main():
    searcher = VisualSearcher("index.pkl")
    evaluator = SearchEvaluator(searcher, "data/coco/annotations/captions_train2017.json")
    
    metrics = evaluator.evaluate_queries(TEST_QUERIES)
    
    print("Mean Average Precision @10:", metrics["MAP@10"])
    print("\nPrecision@K per query:")
    for query, precisions in metrics["Precision@K"].items():
        print(f"'{query}':")
        for k, p in precisions.items():
            print(f"  P@{k}: {p:.3f}")

if __name__ == "__main__":
    main()
