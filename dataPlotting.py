import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("bibi.csv")

df['uploadDate'] = pd.to_datetime(df['uploadDate'])
df.set_index("uploadDate", inplace=True)
df.sort_index(inplace=True)

df["duration"].plot()
plt.show()



"""print(df['region'].unique())

albany_df = df.copy()[df['region']=="Albany"]



albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()
albany_df["price25ma"].plot()
plt.show()"""