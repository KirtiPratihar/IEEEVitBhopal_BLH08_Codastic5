import csv
import random
from datetime import datetime, timedelta

# Define the product names
product_names = ["Sanitary Napkin", "Menstrual Pad", "Panty Liner"]

# Define the NGO donation status
ngo_donation_status = ["Yes", "No"]

# Define the date range for expiry dates
start_date = datetime.now()
end_date = start_date + timedelta(days=365)

# Create a list to store the dummy data
data = []

# Generate 50 dummy data records
for i in range(50):
    product_name = random.choice(product_names)
    expiry_date = (start_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
    quantity = random.randint(50, 200)
    quantity_used = random.randint(10, 50)
    quantity_left = quantity - quantity_used
    ngo_donation = random.choice(ngo_donation_status)
    
    data.append([product_name, expiry_date, quantity, quantity_used, quantity_left, ngo_donation])

# Write the dummy data to a CSV file
with open('period_pads_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Product Name","Date of Expiry","Quantity","Quantity Used","Quantity Left","Donated by NGO"])
    writer.writerows(data)