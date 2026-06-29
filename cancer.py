import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\Admin\Downloads\archive (10)\india_cancer_patients_2022_2025.csv")
df = df[['Patient_ID', 'Age', 'Gender', 'State','Cancer_Type', 'Stage', 'Status']]
df.columns = ['PID', 'Age', 'Gender', 'State','Cancer', 'Stage', 'Status']
print(df.head())
print(df.describe())

sns.barplot(x='Gender', y='Age' ,data=df,hue="Gender")
plt.xticks(rotation= 45)
plt.show()