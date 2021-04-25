import datetime
import pandas as pd
import matplotlib.pyplot as plt
import folium
import folium.plugins as fplug
from IPython.display import display
import os

Path = 'C:\\Users\\Grant\\Desktop\\Random\\CS_Group_Project\\'
Path_alt = "C:/Users/Grant/Desktop/Random/CS_Group_Project/map.html"

week_days_lookup = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

week_days= {"Monday" : 0,"Tuesday" :0 ,"Wednesday": 0,"Thursday": 0,"Friday": 0 ,"Saturday": 0 ,"Sunday": 0 }


terrordata = pd.read_csv(
     Path + 'GDT_2000_2019.csv')


def countWeekdays(year, month, day,counts):
    try:
        weekday=week_days_lookup[datetime.date(year,month,day).weekday()]
        week_days[weekday] = week_days[weekday] + counts
    except:
        pass


collect_dates = terrordata.groupby(['iyear','imonth','iday']).size().reset_index(name='counts')

result = [countWeekdays(row[0],row[1],row[2],row[3]) for row in collect_dates[['iyear','imonth','iday','counts']].to_numpy()]

print(collect_dates.head())
    
print("HERES THE RESULT",week_days)

plt.bar(week_days.keys(), week_days.values())
plt.title('Number of Terrorist Events On Each Day (2000 - 2019)')
plt.xlabel('Weekday')
plt.ylabel('Number of Attacks')
plt.show()


