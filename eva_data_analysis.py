# EVA Data Analysis

### import packages

import json
import datetime as dt
import os
import csv
import matplotlib.pyplot as plt

### file path variables
# https://data.nasa.gov/resource/eva.json (with modifications)
eva_data_json = open('./eva-data.json', 'r')
eva_data_csv = open('./eva-data.csv','w')
g_file = 'cumulative_eva_graph.png'

###  prting and exporting data
fieldnames = ("eva", "country", "crew", "vehicle", "date", "duration", "purpose")

data=[]

for i in range(375):
    line=eva_data_json.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)


w=csv.writer(eva_data_csv)

### processing times

time = []
date =[]


j=0
for i in data:
    print(data[j])
    # and this bit
    w.writerow(data[j].values())
    if 'duration' in data[j].keys():
        duration_str=data[j]['duration']
        if duration_str == '':
            pass
        else:
            duration_date=dt.datetime.strptime(duration_str,'%H:%M')
            duration_time_hr = dt.timedelta(hours=duration_date.hour, minutes=duration_date.minute, seconds=duration_date.second).total_seconds()/(60*60)
            print(duration_date,duration_time_hr)
            time.append(duration_time_hr)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop()
    j+=1

# Build cumulative totals without mutating the list during iteration.
cumulative_time = [0]
for i in time:
    cumulative_time.append(cumulative_time[-1] + i)

date, cumulative_time = zip(*sorted(zip(date, cumulative_time[1:])))

plt.plot(date, cumulative_time, 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(g_file)
plt.show()
