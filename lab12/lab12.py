import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=["A", "B", "C", "D"]
)

report = (
    "Lab 12: Style a Random DataFrame\n\n"
    f"{df.to_string()}\n"
)

with open("lab12_output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(report)

print(report)