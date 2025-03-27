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

A man training the dog in a garden --                                                                                                                     ![image](https://github.com/user-attachments/assets/a6e121e8-14a7-497f-a637-23711deab98c)


 A horse with the saddle on its back --                                                                                                                   ![image](https://github.com/user-attachments/assets/1ccb6481-e5c3-4f2a-89a4-1a5987f15aa9)


People using mobile on roadside --                                                                                                                        ![image](https://github.com/user-attachments/assets/59842bb4-1fc0-45e6-af59-3df7fd68af30)


Cyclists racing through a city street at night --                                                                                                         ![image](https://github.com/user-attachments/assets/b907627f-6948-4b2c-bc88-6711de1c19ac)


A flowervase with blooming flowers --                                                                                                                     ![image](https://github.com/user-attachments/assets/b045345c-f4ea-44f1-8505-a34aa598579a)


A Lighthouse on a rocky coast --                                                                                                                          ![image](https://github.com/user-attachments/assets/5fe3001c-9b79-49e4-988e-fe5e55f0bd33)



### Image search (use sample image)

![image](https://github.com/user-attachments/assets/0fe36bb8-8249-4566-93db-d6b15e60fe10)  --  ![image](https://github.com/user-attachments/assets/9828c7bb-56ba-412a-8127-2fb582452473)

![image](https://github.com/user-attachments/assets/4bc3b2a9-71aa-4e95-a79e-99f536e33a9e)  --  ![image](https://github.com/user-attachments/assets/dab433ca-9bdb-4c3e-8e62-ee8b87fd2e63)

![image](https://github.com/user-attachments/assets/c1128805-8d91-4d95-b44a-7dca50c1ea18)  --  ![image](https://github.com/user-attachments/assets/db68db6f-8435-4547-9267-fbdfb401f234)

![image](https://github.com/user-attachments/assets/18434aa6-3659-4a54-9275-09e6d27d101a)  --  ![image](https://github.com/user-attachments/assets/3fc69826-4e52-4405-b597-8ac27af9484c)

![image](https://github.com/user-attachments/assets/3ed70496-d9a5-4de4-a45d-89a237028220)  --  ![image](https://github.com/user-attachments/assets/b7517b91-a7e2-4929-812a-01854fca1ac1)









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
