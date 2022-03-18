from sys import argv
import json

x = argv[1]
y = argv[2]

with open(x, "r") as tests:
    tests_json = json.load(tests)

with open(y, "r") as values:
    values_json = json.load(values)







for i in tests_json['tests']:

    for v in values_json['values']:
        if i['id'] == v['id']:
            i['value']=v['value']

for i in tests_json['tests'][2]['values']:

    for v in values_json['values']:
        if i['id'] == v['id']:
            i['value']=v['value']

for i in tests_json['tests'][2]['values'][0]['values'][0]['values']:

    for v in values_json['values']:
        if i['id'] == v['id']:
            i['value']=v['value']

for i in tests_json['tests'][2]['values'][1]['values'][0]['values']:

    for v in values_json['values']:
        if i['id'] == v['id']:
            i['value']=v['value']

for i in tests_json['tests'][3]['values']:

    for v in values_json['values']:
        if i['id'] == v['id']:
            i['value']=v['value']



with open("report.json", "w") as write_file:
    json.dump(tests_json, write_file)


























