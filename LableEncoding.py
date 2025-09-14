from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv('sample_data.csv')

df_label = df.copy()


le = LabelEncoder()

df_label['Gender_Ecoded'] = le.fit_transform(df_label['Gender'])

df_label['Passed_Ecoded'] = le.fit_transform(df_label['Passed'])

print("Encoded DataFrame:")
print(df_label[['Name', 'Gender', 'Gender_Ecoded', 'Passed', 'Passed_Ecoded']])
