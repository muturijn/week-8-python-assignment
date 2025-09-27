import os
import pandas as pd
import streamlit as st

st.title("📊 Metadata Dashboard (Lightweight Mode)")

splits_folder = "splits"

def load_data(folder):
    chunks = []
    cols_to_load = ["title", "journal", "publish_time", "abstract", "authors", "license"]  

    if os.path.exists(folder):
        for file in os.listdir(folder):
            if file.endswith(".csv"):
                file_path = os.path.join(folder, file)
                st.write(f"Loading {file} ...")
                try:
                    # Load only selected columns, with chunking
                    for chunk in pd.read_csv(file_path, usecols=cols_to_load, 
                                             chunksize=50000, low_memory=False):
                        chunks.append(chunk)
                except Exception as e:
                    st.error(f"Error reading {file}: {e}")
    if chunks:
        return pd.concat(chunks, ignore_index=True)
    return pd.DataFrame()

# 🚨 No @st.cache_data here (avoids memory pickle issues)
df = load_data(splits_folder)

st.write("### Number of rows loaded:", len(df))

if not df.empty:
    st.write("### Columns:")
    st.write(list(df.columns))

    column = st.selectbox("Select a column to plot", df.columns)

    if column:
        st.write(f"### Value counts for {column}")
        st.bar_chart(df[column].value_counts().head(20))
else:
    st.warning("No data loaded. Please make sure the 'splits' folder contains CSV files.")
