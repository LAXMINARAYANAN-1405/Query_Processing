import pandas as pd

df = pd.read_csv("random_data.csv")

negative_count = int((df.select_dtypes(include="number") < 0).sum().sum())
positive_count = int((df.select_dtypes(include="number") >= 0).sum().sum())

report = (
    "Lab 10: Style Negative and Positive Numbers\n\n"
    f"Negative values: {negative_count}\n"
    f"Non-negative values: {positive_count}\n\n"
    "DataFrame:\n"
    f"{df.to_string(index=True)}\n"
)

with open("lab10_output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(report)

print(report)