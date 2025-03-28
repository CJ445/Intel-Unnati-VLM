# extract_data.py
import os
import zipfile
from tqdm import tqdm

def extract_data():
    print("Starting data extraction...")

    os.makedirs("images", exist_ok=True)

    # Extract annotations (although we won't be using them here, we still extract them)
    print("\nExtracting annotations...")
    annotations_zip = "data/annotations_trainval2017.zip"
    with zipfile.ZipFile(annotations_zip, 'r') as zip_ref:
        zip_ref.extractall("data")

    # Extract images with progress
    print("\nExtracting images...")
    images_zip = "data/train2017.zip"
    with zipfile.ZipFile(images_zip, 'r') as zip_ref:
        all_files = zip_ref.namelist()
        image_files = [f for f in all_files if f.startswith("train2017/") and f.endswith(".jpg")]
        selected_images = image_files[:5000]
        
        for image in tqdm(selected_images, desc="Extracting", unit="img"):
            zip_ref.extract(image, "images")
    
    # Organize files
    os.rename("images/train2017", "images/COCO_train2017")
    
    # Validate
    image_count = len(os.listdir("images/COCO_train2017"))
    print(f"\n✅ Successfully extracted {image_count} images")
    assert image_count == 5000, f"Expected 5000 images, got {image_count}"

if __name__ == "__main__":
    extract_data()
