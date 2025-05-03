import pandas as pd
from PIL import Image
import numpy as np
import os

class DataFileFormat_Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.file_type = None

    def load_data(self):
        ext = os.path.splitext(self.file_path)[1].lower()
        
        if ext == '.csv':
            self.data = pd.read_csv(self.file_path)
            self.file_type = 'tabular'
        elif ext == '.parquet':
            self.data = pd.read_parquet(self.file_path)
            self.file_type = 'tabular'
        elif ext == '.txt':
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = f.read()
            self.file_type = 'text'
        elif ext in ['.jpg', '.jpeg', '.png']:
            self.data = Image.open(self.file_path)
            self.file_type = 'image'
        else:
            raise ValueError(f"Unsupported file format: {ext}. Supported formats: .csv, .parquet, .txt, .jpg, .jpeg, .png")
        
        print(f"Data loaded successfully from {self.file_path} as {self.file_type}.")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")

        print("\n=== Initial Data Summary ===")

        if self.file_type == 'tabular':
            print(self.data.info())
            print("\nMissing Values:")
            print(self.data.isnull().sum())
            print("\nDescriptive Statistics:")
            print(self.data.describe())
        elif self.file_type == 'text':
            print(f"Text Length: {len(self.data)} characters")
            print(f"Preview:\n{self.data[:500]}")
        elif self.file_type == 'image':
            print(f"Image Size: {self.data.size}")
            print(f"Image Mode: {self.data.mode}")
        else:
            print("Unsupported data type for processing.")

def main():
    file_path = 'Week4/image1.png'  # Add File Path (Text, CSV, Parquet, Image)
    processor = DataFileFormat_Processor(file_path)
    processor.load_data()
    processor.initial_processing()

if __name__ == "__main__":
    main()
