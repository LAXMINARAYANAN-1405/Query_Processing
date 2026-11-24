import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=["A", "B", "C", "D"]
)

df.loc[0, "C"] = np.nan
df.loc[3, "D"] = np.nan
df.loc[5, "A"] = np.nan
df.loc[9, "D"] = np.nan

null_locations = [
    f"Row {row}, Column {column}"
    for row, column in zip(*np.where(df.isna()))
]

report = (
    "Lab 11: Display Missing Values\n\n"
    f"Null values: {int(df.isna().sum().sum())}\n"
    "Null locations:\n"
    f"{chr(10).join(null_locations)}\n\n"
    "DataFrame:\n"
    f"{df.to_string()}\n"
)

with open("lab11_output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(report)

print(report)