from sklearn.preprocessing import LabelEncoder
import pandas as pd
df = pd.read_csv('sample_data.csv')

df_label = df.copy()

df_encoded = pd.get_dummies(df_label, columns=['City'])


print("One-Hot Encoded DataFrame:")
print(df_encoded[['Name', 'City_Delhi', 'City_Mumbai', 'City_Kolkata', 'City_Chennai']])