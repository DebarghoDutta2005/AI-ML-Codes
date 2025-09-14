import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, None, 22, None],
    'Salary': [50000, None, 55000, 70000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nChoice 1: Show rows with missing values")
print("Choice 2: Remove rows with missing values")
print("Choice 3: Fill missing values with the mean of the column")
choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    print("\nRows with missing values:")
    print(df[df.isnull().any(axis=1)])
    print("\nPercentage of missing values in each column:")
    print(df.isnull().mean() * 100)
elif choice == 2:
    df_cleaned = df.dropna()
    print("\nDataFrame after removing rows with missing values:")
    print(df_cleaned)
elif choice == 3:
    df_filled = df.fillna(df.mean(numeric_only=True))
    print("\nDataFrame after filling missing values with the mean:")
    print(df_filled)
else:
    print("Invalid choice! Please enter 1, 2, or 3.")
