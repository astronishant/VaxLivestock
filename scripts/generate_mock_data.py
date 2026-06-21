import csv
from datetime import datetime, timedelta
import random

# Headers
headers = [
    'Animal_ID', 'Animal_Type', 'Farmer_Name', 'Assigned_Village', 'GPS_Village',
    'Vaccine_Name', 'Vaccination_Count', 'Time_Taken_Minute', 'Proof_Image_Name',
    'Last_Vaccination_Date', 'Vaccine_Expiry_Date', 'Vaccination_Interval_Days'
]

data = []

# Village list
villages = ['Hosahalli', 'Gollarahatti', 'Chikkaballapura', 'Doddaballapura', 'Tumkur']

today = datetime.now()

# Normal Case (Safe)
data.append([
    'KA-01-9921', 'Cow', 'Ramesh G', 'Hosahalli', 'Hosahalli',
    'FMD Vaccine', '1', '15', 'proof_001.jpg',
    (today - timedelta(days=10)).strftime('%Y-%m-%d'),
    (today + timedelta(days=300)).strftime('%Y-%m-%d'),
    '180'
])

# Overdue Case
data.append([
    'KA-02-4412', 'Buffalo', 'Suresh M', 'Gollarahatti', 'Gollarahatti',
    'Brucellosis', '1', '12', 'proof_002.jpg',
    (today - timedelta(days=200)).strftime('%Y-%m-%d'),
    (today + timedelta(days=100)).strftime('%Y-%m-%d'),
    '180'
])

# Fraud: GPS Mismatch
data.append([
    'KA-03-1122', 'Sheep', 'Anand K', 'Tumkur', 'Doddaballapura',
    'FMD Vaccine', '1', '20', 'proof_003.jpg',
    (today - timedelta(days=5)).strftime('%Y-%m-%d'),
    (today + timedelta(days=360)).strftime('%Y-%m-%d'),
    '180'
])

# Fraud: Impossible Speed
data.append([
    'KA-04-5533', 'Cow', 'Prakash R', 'Chikkaballapura', 'Chikkaballapura',
    'Rabies', '15', '1', 'proof_004.jpg',
    (today - timedelta(days=2)).strftime('%Y-%m-%d'),
    (today + timedelta(days=300)).strftime('%Y-%m-%d'),
    '365'
])

# Fraud: Duplicate Image
data.append([
    'KA-05-9988', 'Cow', 'Manju N', 'Tumkur', 'Tumkur',
    'FMD Vaccine', '1', '15', 'proof_001.jpg', # Duplicate of proof_001.jpg
    (today - timedelta(days=1)).strftime('%Y-%m-%d'),
    (today + timedelta(days=200)).strftime('%Y-%m-%d'),
    '180'
])

# Fraud: Expired Vaccine
data.append([
    'KA-06-3344', 'Buffalo', 'Kumar S', 'Hosahalli', 'Hosahalli',
    'Brucellosis', '1', '10', 'proof_006.jpg',
    (today - timedelta(days=5)).strftime('%Y-%m-%d'),
    (today - timedelta(days=30)).strftime('%Y-%m-%d'), # Expired 30 days ago
    '365'
])

# Due This Week Case
data.append([
    'KA-01-7766', 'Sheep', 'Raju T', 'Gollarahatti', 'Gollarahatti',
    'PPR Vaccine', '1', '14', 'proof_007.jpg',
    (today - timedelta(days=175)).strftime('%Y-%m-%d'),
    (today + timedelta(days=100)).strftime('%Y-%m-%d'),
    '180'
])

with open('livestock_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

print("Generated livestock_data.csv")
