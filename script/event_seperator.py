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

    classified_events = dict()

    for e in event_list:
        st = datetime.strptime(e['start'], "%Y-%m-%d %H:%M:%S")
        key = st.strftime('%Y-%m')
        if key not in classified_events:
            classified_events[key] = dict()
            classified_events[key]['events'] = list()
        classified_events[key]['events'].append(e)

    for k, v in classified_events.items():
        write_file_path = './data/events-' + k + '.json'
        with open(write_file_path, 'w') as f:
            f.write(json.dumps(v, ensure_ascii=False, indent=4))
