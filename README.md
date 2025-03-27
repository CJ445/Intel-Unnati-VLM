# Visual Search using VLM

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

## Demo

```bash
streamlit run app.py
```
### Text search (returns top matches)

A man training the dog in a garden -- ![image](https://github.com/user-attachments/assets/a6e121e8-14a7-497f-a637-23711deab98c)


 A horse with the saddle on its back -- ![image](https://github.com/user-attachments/assets/1ccb6481-e5c3-4f2a-89a4-1a5987f15aa9)


People using mobile on roadside -- ![image](https://github.com/user-attachments/assets/59842bb4-1fc0-45e6-af59-3df7fd68af30)


Cyclists racing through a city street at night -- ![image](https://github.com/user-attachments/assets/b907627f-6948-4b2c-bc88-6711de1c19ac)


A flowervase with blooming flowers -- ![image](https://github.com/user-attachments/assets/b045345c-f4ea-44f1-8505-a34aa598579a)


A Lighthouse on a rocky coast -- ![image](https://github.com/user-attachments/assets/5fe3001c-9b79-49e4-988e-fe5e55f0bd33)



### Image search (use sample image)




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
├── embed.py
├── images (This Directory will be created after running download_data.py)
│   └── COCO_train2017
├── __pycache__
│   └── embed.cpython-310.pyc
├── requirements.txt
└── search.py
```
