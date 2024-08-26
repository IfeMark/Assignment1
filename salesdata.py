import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales.csv")
df.month_number = df.month_number.astype(str)
df['month_number'] = df['month_number'].replace({'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July',
                                                 '8':'August','9':'September','10':'October','11':'November','12':'December'})
df2 = df.rename(columns={'month_number':'month'})
df2list=df2.iloc[:,1:9].sum()
df3 = df2._append(pd.DataFrame([['Total',df2list.iloc[0],df2list.iloc[1],df2list.iloc[2],df2list.iloc[3],df2list.iloc[4],
                                 df2list.iloc[5],df2list.iloc[6],df2list.iloc[7]]],columns=df2.columns),ignore_index = True)
products = (['facecream', 'facewash',  'toothpaste',  'bathingsoap',  'shampoo',  'moisturizer'])
df3list = df3.iloc[:,1:7].sum()
total = df3list
print(df3)

plt.pie(total, labels=products, autopct="%1.2f%%")
plt.axis('equal')
plt.legend()
plt.title('comparism of each product with total units sold')
plt.show()