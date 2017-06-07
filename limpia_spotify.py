import json

with open('../limpio.json') as top50:
	data = json.loads(top50)
	print(data)
