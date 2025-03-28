# Visual Search using VLM

## Run the prebuilt docker image

```bash 
docker run -p 8501:8501 leahtara/visual-search-vlm:dev
```
Open this link in your browser: http://localhost:8501

## Setup locally

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

```bash
streamlit run app.py
```

## Demo
### Text search (returns top matches)
[Insert sample output here]
### Image search (use sample image)
[Insert sample output here]


## To build the docker image yourself
 After setting up locally,
```bash
docker build -t visual-search-image .
```

```bash
docker run -p 8501:8501 visual-search-image
```

## File Structure
```bash
├── chroma_db (This Directory will be created after running chroma_indexer.py)
│   ├── 6a958e2e-303c-4002-a5ba-902ce658afe9
│   └── chroma.sqlite3
├── chroma_indexer.py
├── data (This Directory will be created after running download_data.py)
│   ├── annotations
│   ├── annotations_trainval2017.zip
│   └── train2017.zip
├── download_data.py
├── extract_data.py
├── embed.py
├── images (This Directory will be created after running download_data.py)
│   └── COCO_train2017
├── __pycache__
│   └── embed.cpython-310.pyc
├── requirements.txt
└── search.py
```
