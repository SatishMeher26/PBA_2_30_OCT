import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print("First Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

print("\nStudents Scoring More Than 75:")
print(df[df["Marks"] > 75])

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

plt.hist(df["Marks"], bins=5)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
