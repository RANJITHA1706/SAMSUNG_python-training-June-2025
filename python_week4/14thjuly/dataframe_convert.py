import os
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)
csv_filename = "data_sample.csv"
df.to_csv(csv_filename, index = False)
print(f"DataFrame saved as :{csv_filename}")

if os.path.exists(csv_filename):
    print("\n File exists. Reading content using os module:\n")
    with open(csv_filename, 'r') as f:
        content = f.read()
        print(content)
else:
    print("File not found")