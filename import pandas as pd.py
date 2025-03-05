import pandas as pd

# Sample data
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"],
    "Age": [30, 35, 28, 32, 40, 45, 29, 38, 26, 33],
    "Gender": ["Female", "Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Salary": [70000, 80000, 65000, 75000, 90000, 85000, 72000, 78000, 60000, 77000],
    "Department": ["HR", "Engineering", "Marketing", "Finance", "Engineering", "HR", "Marketing", "Finance", "Engineering", "Marketing"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sample_data.csv", index=False)

print("CSV file 'sample_data.csv' has been created successfully.")
