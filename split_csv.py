import pandas as pd
import os

# Path to your large CSV
input_csv = r"C:\Users\user\Documents\metadata.csv\clean_metadata.csv"

# Folder to store split CSVs
output_folder = r"C:\Users\user\Documents\metadata.csv\splits"
os.makedirs(output_folder, exist_ok=True)

# Number of rows per split
chunk_size = 200000  # adjust if needed

# Split and save
for i, chunk in enumerate(pd.read_csv(input_csv, chunksize=chunk_size)):
    chunk.to_csv(os.path.join(output_folder, f"metadata_part_{i}.csv"), index=False)

print(f"CSV split complete. Files saved in {output_folder}")
