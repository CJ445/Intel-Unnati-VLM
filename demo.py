from search import VisualSearcher
searcher = VisualSearcher("data/index.pkl")

# Text Search
print("=== Text Search ===")
for result in searcher.search_by_text("black dog playing in snow", k=3):
    print(f"Score: {result[1]:.3f} | Image: {result[0].split('/')[-1]}")

# Image Search (using first image as query)
print("\n=== Image Search ===")
sample_image = "data/coco/images/COCO_train2017_000000000009.jpg"
for result in searcher.search_by_image(sample_image, k=3):
    print(f"Score: {result[1]:.3f} | Image: {result[0].split('/')[-1]}")
