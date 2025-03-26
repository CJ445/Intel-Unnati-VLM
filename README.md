# Intel-Unnati-VLM

## Dataset preparation

```
git clone https://github.com/CJ445/Intel-Unnati-VLM
cd Intel-Unnati-VLM
```

```
mkdir -p data/coco
cd data/coco
```
### Download dataset

```
# Download COCO 2017 annotations (captions)
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
unzip annotations_trainval2017.zip

# Download exactly 5,000 images (parallel download)
aria2c -x16 -s16 -i sampled_image_ids.txt \
       --dir=images \
       --out="COCO_train2017_{}.jpg" \
       --force-sequential=true \
       --allow-overwrite=true \
       --auto-file-renaming=false \
       --input-file=<(awk '{print "http://images.cocodataset.org/train2017/" sprintf("%012d", $1) ".jpg"}' sampled_image_ids.txt)
```

### Prerequisite: Install aria2 for parallel downloads:
```
    sudo apt install aria2  # Ubuntu/Debian
```
### File Structure:
```
    data/coco/
    ├── images/               # 5,000 images
    ├── annotations/
    │   ├── captions_train2017.json  # All captions
    └── sampled_image_ids.txt  # Your 5K image IDs
```
### Verification:
```
    # Check image count
    ls images | wc -l  # Should output 5000

    # Check captions
    head -n 20 annotations/captions_train2017.json | grep "caption"

```
