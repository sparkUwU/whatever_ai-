import numpy as np
import pandas as pd

names = ["Alice", "Bob", "John"]
student_scores = np.array([85, 92, 78])

df = pd.DataFrame({
    "Name": names, 
    "Score": student_scores})

average_score = df["Score"].mean()
print(f"Average Score: {average_score}")

max_score = df["Score"].max()
print(f"Max Score: {max_score}")

min_score = df["Score"].min()
print(f"Min Score: {min_score}")

top_scorer = df.loc[df["Score"].idxmax(), "Name"]
print(f"Top Scorer: {top_scorer}")

print("\nStudent Scores Table:\n")
print(df)