import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("weather2.csv",encoding = 'latin 1') 
df = df.rename(columns={'Day':'Date'})
df['Average Temperature (°F)'] = round((df.iloc[:,1:3].sum(axis=1))/2)
df['Average Humidity (°F)'] = round((df.iloc[:,3:5].sum(axis=1))/2)
df['Year'] = pd.DatetimeIndex(df['Date']).year
df['Date'] = pd.to_datetime(df['Date'], dayfirst= True, format= 'mixed')
df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')
print(f"This is the edited dataset: \n{df}")

L_temp = []
L_max_temp = []
L_humidity = []
L_max_humidity = []
year = 2009
L_years = []
for index, row in df.iterrows():
    if index < len(df['Year'])-1:
        if row['Year'] == year:
            L_temp.append(row.iloc[5])
            L_humidity.append(row.iloc[6])
        else:
            print(f"For year: {year}")
            print(f"The highest temperature is {max(L_temp)}")
            print(f"The highest humidity is {max(L_humidity)}")
            print(f"The lowest temperature is {min(L_temp)}")
            print(f"The lowest humidity is {min(L_humidity)}\n")
            L_max_temp.append(max(L_temp))
            L_max_humidity.append(max(L_humidity))
            L_temp.clear()
            L_humidity.clear()
            L_years.append(year)
            year+=1
            L_temp.append(row.iloc[5])
            L_humidity.append(row.iloc[6])
    else:
        print(f"For year: {year}")
        print(f"The highest temperature is {max(L_temp)}")
        print(f"The highest humidity is {max(L_humidity)}")
        print(f"The lowest temperature is {min(L_temp)}")
        print(f"The lowest humidity is {min(L_humidity)}\n")
        L_max_temp.append(max(L_temp))
        L_max_humidity.append(max(L_humidity))
        L_years.append(year)
 
fig, axs = plt.subplots(2,2)       
axs[0,0].plot(L_years, L_max_temp)
axs[0,0].set_title("Comparism of the highest temperature of each years")
axs[0,1].hist(sorted(df['Average Temperature (°F)']), bins = 5, edgecolor = 'black')
axs[0,1].set_title("Frequency of temperatures for the past 10 years")
axs[1,0].plot(L_years, L_max_humidity)
axs[1,0].set_title("comparism of the highest humidity of each years")
axs[1,1].hist(sorted(L_max_humidity), bins = 5, edgecolor = 'black')
axs[1,1].set_title("Frequency of humdity for the past 10 years")
print(plt.show())
