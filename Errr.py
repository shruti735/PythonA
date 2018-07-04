import json
val = input("Input Something :")

data=json.loads(val)
print("Python Data - ",data)
print("JSON DAta ",json.dumps(data))
print(val)
