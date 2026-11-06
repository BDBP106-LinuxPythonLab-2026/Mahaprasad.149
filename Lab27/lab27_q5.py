import pandas as pd

df = pd.read_csv("diabetes.csv")

# (i) Column names
print(df.columns)

# (ii) First 10 rows
print(df.head(10))

# (iii) Mean blood pressure
print(df["BloodPressure"].mean())

# (iv) First 4 rows of columns 3, 4, 5
print(df.iloc[:4, 2:5])

# (v) Normalize BP
BP = df["BloodPressure"]
df["NormalizedBP"] = (BP-BP.min())/(BP.max()-BP.min())

# (vi) Age category
def categorize_age(age):
    if age <= 18:
        return "Youth"
    elif age <= 50:
        return "Adult"
    else:
        return "Senior"

df["age category"] = df["Age"].apply(categorize_age)

print(df.head())
