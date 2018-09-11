# -*- coding:utf-8 -*-
import json
from datetime import datetime
from collections import OrderedDict


def sorting_dict_by_key(src_dict, reverse=False):
    return _sorting_dict(src_dict=src_dict, sorting_index=0, reverse=reverse)


def sorting_dict_by_value(src_dict, reverse=False):
    return _sorting_dict(src_dict=src_dict, sorting_index=1, reverse=reverse)


def _sorting_dict(src_dict, sorting_index=0, reverse=False):
    return dict(OrderedDict(sorted(src_dict.items(), key=lambda t: t[sorting_index], reverse=reverse)))


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
    week_day_result = dict()

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
        week_day_key = st.weekday()
        date_key = st.strftime('%Y-%m-%d')
        month_key = st.strftime('%m')
        if date_key not in date_result:
            date_result[date_key] = 0
        date_result[date_key] += 1

        # month
        if month_key not in month_result:
            month_result[month_key] = 0
        month_result[month_key] += 1

        # week_day_result
        if week_day_key not in week_day_result:
            week_day_result[week_day_key] = 0
        week_day_result[week_day_key] += 1

    tag_result = sorting_dict_by_value(src_dict=tag_result, reverse=True)
    date_result = sorting_dict_by_key(src_dict=date_result, reverse=True)
    month_result = sorting_dict_by_key(src_dict=month_result, reverse=False)
    week_day_result = sorting_dict_by_key(src_dict=week_day_result, reverse=False)

    statistic = {
        'tag': tag_result,
        'date': date_result,
        'month': month_result,
        'weekday': week_day_result
    }

    write_file_path = './data/statistic.json'
    with open(write_file_path, 'w') as f:
        f.write(json.dumps(statistic, ensure_ascii=False, indent=4))
