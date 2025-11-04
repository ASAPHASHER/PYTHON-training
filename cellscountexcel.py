import pandas as pd

file = "data.xlsx"
df = pd.read_excel(file) 
total_cells = df.shape[0] * df.shape[1]
print("Total cells:", total_cells)
print("Sum of numbers:", df.sum().sum())