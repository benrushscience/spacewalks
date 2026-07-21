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

entries = []

for record in data:
    print(record)
    w.writerow(record.values())

    duration_str = record.get('duration', '')
    date_str = record.get('date', '')
    if not duration_str or not date_str:
        continue

    duration_date = dt.datetime.strptime(duration_str, '%H:%M')
    duration_time_hr = dt.timedelta(
        hours=duration_date.hour,
        minutes=duration_date.minute,
        seconds=duration_date.second,
    ).total_seconds() / (60 * 60)
    eva_date = dt.datetime.strptime(date_str[0:10], '%Y-%m-%d')
    entries.append((eva_date, duration_time_hr))

# Sort by date first, then compute cumulative time in chronological order.
entries.sort(key=lambda item: item[0])

date = []
cumulative_time = []
running_total = 0
for eva_date, duration_hr in entries:
    running_total += duration_hr
    date.append(eva_date)
    cumulative_time.append(running_total)

plt.plot(date, cumulative_time, 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(g_file)
plt.show()
