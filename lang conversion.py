import json
jsonData = '{"name":"frank","age": 39,"address":true}'
var=json.loads(jsonData)

print(var)
print(json.dumps(var ))
