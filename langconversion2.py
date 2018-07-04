import json
jsonData = '{"101":{"name": "V","class": "V","address":7},'\
             '"102":{"name": "S","class": "V","address":8},'\
             '"103":{"name": "A","class": "V","address":12}}'
var=json.loads(jsonData)

print(var)
print(json.dumps(jsonData))
