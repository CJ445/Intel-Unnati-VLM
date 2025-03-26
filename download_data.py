import os
import zipfile
import urllib.request
from tqdm import tqdm

COCO_IMAGES_URL = "http://images.cocodataset.org/zips/train2017.zip"
COCO_ANNOTATIONS_URL = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_file(url, output_path):
    if not os.path.exists(output_path):
        print(f"\nDownloading {os.path.basename(output_path)}...")
        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1) as t:
            urllib.request.urlretrieve(url, output_path, reporthook=t.update_to)
        print(f"Saved to {output_path}")
    else:
        print(f"File exists: {output_path}")

def download_coco_data():
    print("Starting COCO dataset download...")
    os.makedirs("data", exist_ok=True)
    os.makedirs("images", exist_ok=True)
    
    # Download annotations
    annotations_zip = "data/annotations_trainval2017.zip"
    download_file(COCO_ANNOTATIONS_URL, annotations_zip)
    
    # Extract annotations
    print("\nExtracting annotations...")
    with zipfile.ZipFile(annotations_zip, 'r') as zip_ref:
        zip_ref.extractall("data")
    
    # Download images
    images_zip = "data/train2017.zip"
    download_file(COCO_IMAGES_URL, images_zip)
    
    # Extract images with progress
    print("\nExtracting images...")
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
    print(f"\n✅ Successfully downloaded {image_count} images")
    assert image_count == 5000, f"Expected 5000 images, got {image_count}"

if __name__ == "__main__":
    download_coco_data()
