# Visual Search using VLM

## Setup

```bash
git clone https://github.com/CJ445/Intel-Unnati-VLM
cd Intel-Unnati-VLM
```

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
python download_data.py
```

```bash
python chroma_indexer.py
```

## Demo

```bash
python search.py "a man in a suit" --k 3
```
```bash
python search.py "a birthday party" --k 3
```
```bash
python search.py "a slice of pizza" --k 3
```
```bash
python search.py "a black cat outdoors" --k 3
```
```bash
python search.py "a glass of wine" --k 3
```
```bash
python search.py "a flower outisde" --k 3
```

## File Structure

```bash
├── chroma_db
│   ├── 6a958e2e-303c-4002-a5ba-902ce658afe9
│   └── chroma.sqlite3
├── chroma_indexer.py
├── data
│   ├── annotations
│   ├── annotations_trainval2017.zip
│   └── train2017.zip
├── download_data.py
├── embed.py
├── images
│   └── COCO_train2017
├── __pycache__
│   └── embed.cpython-310.pyc
├── requirements.txt
├── search.py
├── setup.md
└── validate_system.py
```
