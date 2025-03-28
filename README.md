# Visual Search using VLM
This project builds a vector database of tags for 5,000 images and allows users to search the database by input. It then displays the images that are most similar based on the tags.

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
![image](https://github.com/user-attachments/assets/afd9ed61-e84b-42c4-abcb-c7dd83785ab2)
### Image search (use sample image)
![image](https://github.com/user-attachments/assets/2743c078-eccf-467b-85af-f28f7cad2c8b)


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
