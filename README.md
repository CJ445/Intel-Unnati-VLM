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
### Prerequisite: Install aria2 for parallel downloads:
```
sudo apt install aria2  # Ubuntu/Debian
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
### File Structure:
```
├── data
│   └── coco
│       ├── annotations
│       ├── annotations_trainval2017.zip
│       ├── images
│       └── sampled_image_ids.txt
├── demo.py
├── embedding_utils.py
├── evaluate.py
├── indexing.py
├── project_scope.md
├── __pycache__
│   ├── embedding_utils.cpython-312.pyc
│   ├── indexing.cpython-312.pyc
│   └── search.cpython-312.pyc
└── search.py

```
### Verification:
```
# Check image count
ls images | wc -l  # Should output 5000
# Check captions
head -n 20 annotations/captions_train2017.json | grep "caption"
```
