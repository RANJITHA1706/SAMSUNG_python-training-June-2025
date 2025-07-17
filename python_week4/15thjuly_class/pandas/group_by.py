# Grouping by Department and calculating mean, sum, and max salary
import pandas as pd
data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [60000, 55000, 70000, 58000, 75000]
}

df = pd.DataFrame(data)
grouped_df = df.groupby('Department').agg({'Salary': ['mean', 'sum', 'max']})  
print(grouped_df)

