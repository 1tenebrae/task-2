import json

with open("data.json", "r") as data:
	data = json.load(data)

departs_list = []
for i in data:
	if i['dept'] not in departs_list:
		departs_list.append(i['dept'])


all_depart_people = []
for i in departs_list:
	depart_people = []
	for j in data:
		if j['dept'] == i:
			depart_people.append(j)
	all_depart_people.append(depart_people)


all_avg_hours = []
all_count_people = []
for i in all_depart_people:
	counter_people = 0
	counter_hours = 0
	sum_hours = 0
	avg_hours = 0
	for j in i:
		counter_people += 1
		j.pop('dept')
		if 'hours' in j.keys():
			counter_hours += 1
			sum_hours += j['hours']
	avg_hours = int(sum_hours/counter_hours + 0.5)
	all_count_people.append(counter_people)
	all_avg_hours.append(avg_hours)

result_python = {}

for i in departs_list:
	index_elem = departs_list.index(i)
	result_python[i] = {
	"count" : all_count_people[index_elem],
	"avg_hours" : all_avg_hours[index_elem],
	"people" : all_depart_people[index_elem]
	}

result_json = json.dumps(result_python, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

print(result_json)

with open('output.json', 'w') as result:
    json.dump(result_python, result, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))

input('Press ENTER to exit')