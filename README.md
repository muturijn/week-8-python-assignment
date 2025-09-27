# 📊 Metadata Dashboard

A lightweight **Streamlit dashboard** for exploring a large `metadata.csv` dataset by splitting it into smaller parts and visualizing columns interactively.

---

## 🚀 Features
- Handles very large CSVs by splitting them into smaller chunks.
- Interactive column selection for visualization.
- Displays **value counts** for chosen columns.
- Designed for limited-memory environments (avoids full dataset load).

---

## 🗂️ Project Structure
metadata.csv/
│── app.py # Main Streamlit app
│── split_csv.py # Script to split large CSV into smaller parts
│── splits/ # Folder containing split CSVs (metadata_part_0.csv, etc.)
│── README.md # Documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

1. **Clone or copy** this project into a folder.

2. **Install dependencies** (preferably in a virtual environment):
   ```bash
   pip install streamlit pandas
Split the dataset (if not already done):

bash
Copy code
python split_csv.py
This creates smaller CSVs inside the splits/ folder.

Run the dashboard:

bash
Copy code
streamlit run app.py
📝 Usage
Start the app with Streamlit.

Select a column from the dropdown.

View value counts and quick plots for that column.

💡 Code Documentation
split_csv.py
python
Copy code
# Splits a large CSV into smaller chunks for easier processing
import pandas as pd
import os

input_csv = r"C:\Users\user\Documents\metadata.csv\clean_metadata.csv"
output_folder = r"C:\Users\user\Documents\metadata.csv\splits"
os.makedirs(output_folder, exist_ok=True)

chunk_size = 200000  # rows per split

# Split into chunks
for i, chunk in enumerate(pd.read_csv(input_csv, chunksize=chunk_size, low_memory=False)):
    chunk.to_csv(os.path.join(output_folder, f"metadata_part_{i}.csv"), index=False)

print(f"CSV split complete. Files saved in {output_folder}")
app.py
python
Copy code
# Streamlit app to load split CSVs and allow interactive exploration
import streamlit as st
import pandas as pd
import os

DATA_FOLDER = "splits"

@st.cache_data
def load_data():
    dfs = []
    for file in sorted(os.listdir(DATA_FOLDER)):
        if file.endswith(".csv"):
            try:
                st.write(f"Loading {file} ...")
                df = pd.read_csv(os.path.join(DATA_FOLDER, file), usecols=["title","license","abstract","publish_time","authors","journal"])
                dfs.append(df)
            except Exception as e:
                st.error(f"Error reading {file}: {e}")
    return pd.concat(dfs, ignore_index=True)

st.title("📊 Metadata Dashboard (Lightweight Mode)")

df = load_data()

st.write(f"Number of rows loaded: {len(df)}")
st.write("Columns:", list(df.columns))

col = st.selectbox("Select a column to plot", df.columns)
if col:
    st.write(f"Value counts for {col}")
    st.write(df[col].value_counts().head(20))
📑 Findings
The dataset contains over 820,000 rows.

Important metadata fields: title, license, abstract, publish_time, authors, journal.

Splitting the dataset allowed processing without running into memory errors.

🤔 Challenges & Reflections
Challenges
Memory Errors: Could not load the dataset fully due to limited system RAM.

Large CSV Handling: Needed to split the file into smaller manageable parts.

Performance: Streamlit slowed down with too many rows.

Solutions
Implemented CSV splitting using Pandas chunks.

Reduced columns loaded with usecols for efficiency.

Used Streamlit’s @st.cache_data to avoid reloading data repeatedly.

Reflection
This project taught me:

How to handle big data in Python with limited resources.

The importance of optimizing memory usage.

How to create an interactive dashboard for large-scale datasets.

Practical experience with Streamlit and Pandas in real-world scenarios.
