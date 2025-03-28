FROM python:3.10-slim

WORKDIR /app

# Install system dependencies first
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copy all files (more reliable than using *)
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -i https://pypi.org/simple -r requirements.txt

# Install Streamlit
RUN pip install streamlit

# Run Python scripts during the build process
RUN python download_data.py
RUN python chroma_indexer.py

# Expose port 8501 for Streamlit
EXPOSE 8501

# Default command to run Streamlit app when the container starts
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true"]
