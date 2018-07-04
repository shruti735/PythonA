import json
jsonData = '{"countercode":"100","batch":[{"name":"shruti","fee":2000},' \
                                         '{"name": "shru", "fee": 8000},' \
                                         '{"name":"uti","fee":7000}]}'
var = json.loads(jsonData)

print(var)

