# download_data.py
import os
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

    # Download annotations
    annotations_zip = "data/annotations_trainval2017.zip"
    download_file(COCO_ANNOTATIONS_URL, annotations_zip)
    
    # Download images
    images_zip = "data/train2017.zip"
    download_file(COCO_IMAGES_URL, images_zip)

if __name__ == "__main__":
    download_coco_data()
