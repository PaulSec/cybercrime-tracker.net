import matplotlib.pyplot as plt
import collections
import json

limit = 10
# Feeding process
with open('dump.json') as f:
	data = json.loads(f.read())
stats = {}
for item in data:
	# if '-2014' in item['date']:
	if item['type'] not in stats:
		stats[item['type']] = 1
	else:
		stats[item['type']] = stats[item['type']] + 1
# Data to plot
sorted_stats = sorted(stats, key=stats.__getitem__)[::-1]

labels = sorted_stats[:limit]
sizes = []
for label in labels:
	sizes.append(stats[label])
print(sizes)
# labels = ['Python', 'C++', 'Ruby', 'Java']
# sizes = [215, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0)
for i in range(0, limit - 2):
	explode = explode + (0, )
print(explode)
# Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()