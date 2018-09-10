# -*- coding:utf-8 -*-
import json
from datetime import datetime
json_data_file_path = './data/events.json'

events = None

with open(json_data_file_path, 'r') as f:
    events = f.read()

if events:
    events_json = json.loads(events, encoding="utf-8")
    event_list = events_json['events']

    tag_result = dict()
    date_result = dict()
    month_result = dict()

    for e in event_list:
        # tag
        tag_list = e['tags'].split(',')
        for tag_key in tag_list:
            tag_key = tag_key.strip().lower()
            if tag_key not in tag_result:
                tag_result[tag_key] = 0
            tag_result[tag_key] += 1

        # date
        st = datetime.strptime(e['start'], "%Y-%m-%d %H:%M:%S")
        date_key = st.strftime('%Y-%m-%d')
        month_key = st.strftime('%Y-%m')
        if date_key not in date_result:
            date_result[date_key] = 0
        date_result[date_key] += 1

        # month
        if month_key not in month_result:
            month_result[month_key] = 0
        month_result[month_key] += 1

    from collections import OrderedDict

    tag_result = dict(OrderedDict(sorted(tag_result.items(), key=lambda t: t[1], reverse=True)))
    date_result = dict(OrderedDict(sorted(date_result.items(), key=lambda t: t[0], reverse=True)))
    month_result = dict(OrderedDict(sorted(month_result.items(), key=lambda t: t[0], reverse=True)))
    statistic = {
        'tag': tag_result,
        'date': date_result,
        'month': month_result
    }
    write_file_path = './data/statistic.json'
    with open(write_file_path, 'w') as f:
        f.write(json.dumps(statistic, ensure_ascii=False, indent=4))
