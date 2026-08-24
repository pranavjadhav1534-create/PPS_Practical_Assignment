import numpy as np
import pandas as pd


raw_data = {
    "Student_ID": [201, 202, 203, 204, 204, 205, 206],

    "Full Name": [
        "  Rahul Patil ",
        "Sneha Sharma",
        "  Amit Joshi",
        "Priya Kulkarni",
        "Priya Kulkarni",
        "Rohan Deshmukh",
        "Neha More"
    ],

    "Department": [
        "Computer",
        "Electronics",
        "Mechanical",
        "Computer",
        "Computer",
        None,
        "Electronics"
    ],

    "Age": [18, 19, np.nan, 20, 20, 18, 19],

    "Marks": [85, 72, 91, 68, 68, np.nan, 78],

    "Attendance": [92, 85, 88, np.nan, np.nan, 76, 90],

    "Admission_Date": [
        "2024-08-15",
        "2024-08-16",
        "2024-08-20",
        "2024-08-15",
        "2024-08-15",
        "2024-08-22",
        "2024-08-18"
    ]
}

df = pd.DataFrame(raw_data)

print("\n--- ORIGINAL DATAFRAME ---")
print(df)

print("\n" + "=" * 60)

duplicate_count = df.duplicated().sum()
print(f"Number of duplicated rows found: {duplicate_count}")

df_cleaned = df.drop_duplicates().copy()

print("\nMissing Values Per Column:")
print(df_cleaned.isnull().sum())

median_age = df_cleaned["Age"].median()

print(f"Median Age: {median_age}")
print("\n" + "=" * 60)




