import pandas as pd

df = pd.read_csv("../data/cleaned_housing_data.csv")

# Price per sqft
df['price_per_sqft'] = df['ticket_price_cr'] * 10000000 / df['super_builtup_area']

# Booking flag
df['booking_flag'] = df['booking_status'].apply(lambda x: 1 if x == "Booked" else 0)

# Quarter number
df['quarter_number'] = df['purchase_quarter'].str.extract('(\d)').astype(int)

df.to_csv("../data/final_dataset.csv", index=False)

print("Feature engineering completed")