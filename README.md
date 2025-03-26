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
