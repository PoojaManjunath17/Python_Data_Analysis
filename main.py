import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\Admin\Downloads\archive (7)\covid_19_india.csv")
df = df[['Date', 'State/UnionTerritory', 'Deaths', 'Cured', 'Confirmed']]
df.columns = ['Dt', 'St', 'Dth', 'Crd', 'Cfm']
print(df.head())
print(df.describe())
maxdt = df.sort_values(by='Dth', ascending=False)
print(maxdt.head())
tsd=maxdt[0:5]
print(tsd)
tsd=maxdt[0:10]
print(tsd)

sns.barplot(x='St', y='Dth', data=tsd)
plt.show()
'''maxdt=today.sort_value(by-'Dth')
print(maxdt)'''
'''print("Mean:", df["Confirmed"].mean())
print("Standard Deviation:", df["Confirmed"].std()) '''