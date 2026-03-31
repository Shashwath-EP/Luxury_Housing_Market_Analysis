import os
import pandas as pd
import numpy as np

# Set standard relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "housing_data.csv")
output_path = os.path.join(script_dir, "..", "data", "cleaned_housing_data.csv")

# Load dataset
df = pd.read_csv(data_path)

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Convert ticket price to numeric (handling '₹' and 'Cr' symbols)
df['ticket_price_cr'] = df['ticket_price_cr'].astype(str).str.replace('₹', '', regex=False).str.replace('Cr', '', regex=False).str.replace(',', '', regex=False).str.strip()
df['ticket_price_cr'] = pd.to_numeric(df['ticket_price_cr'], errors='coerce')

# Handle missing values
df['amenity_score'] = df['amenity_score'].fillna(df['amenity_score'].median())
df['possession_status'] = df['possession_status'].fillna("Unknown")

# Normalize text fields
df['developer_name'] = df['developer_name'].str.title().str.strip()
df['micro_market'] = df['micro_market'].str.title().str.strip()

# Save cleaned dataset
df.to_csv(output_path, index=False)

print("Data cleaning completed")