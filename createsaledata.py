import pandas as pd
import random
from datetime import datetime, timedelta

# Ensure datetime is defined before using it
if 'datetime' not in globals():
    from datetime import datetime, timedelta

# Generate sample sales data
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys']
start_date = datetime(2024, 1, 1)

data = []
for i in range(100):
    date = start_date + timedelta(days=i)
    category = random.choice(categories)
    sales = round(random.uniform(500, 5000), 2)
    data.append([date.strftime('%Y-%m-%d'), category, sales])

# Create DataFrame
df = pd.DataFrame(data, columns=['Date', 'Category', 'Sales'])

# Save to CSV
df.to_csv("sales_data.csv", index=False)

print("sales_data.csv has been created successfully.")
