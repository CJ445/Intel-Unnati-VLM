import streamlit as st
from search import VisualSearcher
import os
from PIL import Image
import math

# Initialize searcher and session state
if 'searcher' not in st.session_state:
    st.session_state.searcher = VisualSearcher()
if 'page' not in st.session_state:
    st.session_state.page = 0

# Constants
IMAGES_PER_PAGE = 12
image_dir = "images/COCO_train2017"
image_files = sorted(os.listdir(image_dir))
image_paths = [os.path.join(image_dir, img) for img in image_files]
total_pages = math.ceil(len(image_paths) / IMAGES_PER_PAGE)

# UI Layout
st.set_page_config(layout="wide")
st.title("Visual Search Engine")

# Navigation
tab1, tab2 = st.tabs(["Text Search", "Image Search"])

with tab1:
    st.header("Text Query")
    text_query = st.text_input("Enter your text query:", "a red car")
    k_text = st.slider("Number of results (Text):", 1, 10, 3)
    
    if st.button("Search Text"):
        results, latency = st.session_state.searcher.search_by_text(text_query, k_text)
        st.write(f"Results (Latency: {latency:.1f}ms):")
        
        cols = st.columns(k_text)
        for idx, (path, score) in enumerate(results):
            with cols[idx]:
                st.image(path, caption=f"Score: {score:.3f}", width=200)
                st.write(os.path.basename(path))

with tab2:
    st.header("Image Query")
    
    # Pagination controls
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("Previous") and st.session_state.page > 0:
            st.session_state.page -= 1
    with col2:
        st.write(f"Page {st.session_state.page + 1} of {total_pages}")
    with col3:
        if st.button("Next") and st.session_state.page < total_pages - 1:
            st.session_state.page += 1
    
    # Display current page of images
    start_idx = st.session_state.page * IMAGES_PER_PAGE
    end_idx = start_idx + IMAGES_PER_PAGE
    current_images = image_paths[start_idx:end_idx]
    
    # Create 3x4 grid (12 images)
    for i in range(0, len(current_images), 4):
        cols = st.columns(4)
        for j in range(4):
            idx = i + j
            if idx < len(current_images):
                with cols[j]:
                    # Use radio buttons for selection
                    st.image(
                        current_images[idx], 
                        width=150,
                        caption=os.path.basename(current_images[idx])
                    )
                    if st.button(f"Select", key=f"select_{idx}"):
                        st.session_state.selected_image = current_images[idx]
    
    # Show selected image and search
    if 'selected_image' in st.session_state:
        st.divider()
        st.subheader("Selected Image")
        st.image(st.session_state.selected_image, width=300)
        
        k_image = st.slider("Number of results (Image):", 1, 10, 3)
        
        if st.button("Search Similar Images"):
            # Store results in session state to prevent disappearance
            st.session_state.results, st.session_state.latency = st.session_state.searcher.search_by_image(
                st.session_state.selected_image, k_image
            )
    
    # Display results if they exist
    if 'results' in st.session_state:
        st.divider()
        st.subheader("Search Results")
        st.write(f"Results (Latency: {st.session_state.latency:.1f}ms):")
        
        cols = st.columns(len(st.session_state.results))
        for idx, (path, score) in enumerate(st.session_state.results):
            with cols[idx]:
                st.image(path, caption=f"Score: {score:.3f}", width=200)
                st.write(os.path.basename(path))
