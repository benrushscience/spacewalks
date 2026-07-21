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
        tt=data[j]['duration']
        if tt == '':
            pass
        else:
            t=dt.datetime.strptime(tt,'%H:%M')
            ttt = dt.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()/(60*60)
            print(t,ttt)
            time.append(ttt)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

t=[0]
for i in time:
    t.append(t[-1]+i)

date,time = zip(*sorted(zip(date, time)))

plt.plot(date,t[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(g_file)
plt.show()
