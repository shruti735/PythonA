import json

array1 = '["one", "two"]'
array2 = '["shruti", "soumya"]'


def join2array(array1, array2):
    pass
    list1 = json.loads ( array1 )
    list2 = json.loads ( array2 )
    return json.dumps ( list1 + list2 )

var = join2array( array1, array2)
print ( var )
