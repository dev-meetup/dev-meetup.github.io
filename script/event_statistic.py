# -*- coding:utf-8 -*-
import json
from collections import defaultdict
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

    tag_result = defaultdict(lambda: 0)
    date_result = defaultdict(lambda: 0)
    month_result = defaultdict(lambda: 0)
    week_day_result = defaultdict(lambda: 0)
    st_hour_result = defaultdict(lambda: 0)
    ed_hour_result = defaultdict(lambda: 0)

    for e in event_list:
        st = datetime.strptime(e['start'], "%Y-%m-%d %H:%M:%S")
        ed = datetime.strptime(e['end'], "%Y-%m-%d %H:%M:%S")

        # tag
        tag_list = e['tags'].split(',')
        for tag_key in tag_list:
            tag_key = tag_key.strip().lower()
            tag_result[tag_key] += 1

        # keys :  date & weekday & month & st & ed
        week_day_key = st.weekday()
        date_key = st.strftime('%Y-%m-%d')
        month_key = st.strftime('%m')
        st_hour_key = st.strftime('%H')
        ed_hour_key = ed.strftime('%H')

        # date
        date_result[date_key] += 1

        # month
        month_result[month_key] += 1

        # week_day_result
        week_day_result[week_day_key] += 1

        # st_hour_result
        st_hour_result[st_hour_key] += 1

        # ed_hour_result
        ed_hour_result[ed_hour_key] += 1

    # sorting
    tag_result = sorting_dict_by_value(src_dict=tag_result, reverse=True)
    date_result = sorting_dict_by_key(src_dict=date_result, reverse=True)
    month_result = sorting_dict_by_key(src_dict=month_result, reverse=False)
    week_day_result = sorting_dict_by_key(src_dict=week_day_result, reverse=False)
    st_hour_result = sorting_dict_by_key(src_dict=st_hour_result, reverse=False)
    ed_hour_result = sorting_dict_by_key(src_dict=ed_hour_result, reverse=False)
    hour_keys = ["%02d" % i for i in range(0, 24)]

    for hour_key in hour_keys:
        if hour_key not in st_hour_result:
            st_hour_result[hour_key] = 0
        if hour_key not in ed_hour_result:
            ed_hour_result[hour_key] = 0

    statistic = {
        'tag': tag_result,
        'date': date_result,
        'month': month_result,
        'weekday': week_day_result,
        'st_hour': st_hour_result,
        'ed_hour': ed_hour_result
    }

    sorted_tags = sorted(tag_result.keys())
    tags = {
        'tags': sorted_tags
    }

    write_file_path = './data/statistic.json'
    with open(write_file_path, 'w') as f:
        f.write(json.dumps(statistic, ensure_ascii=False, indent=4))

    write_file_path = './data/tags.json'
    with open(write_file_path, 'w') as f:
        f.write(json.dumps(tags, ensure_ascii=False, indent=4))
