def get_distance(speed,duration):
	distanceinkm=speed*duration
	distanceinm=distanceinkm*1000
	return distanceinm
print(get_distance(12,34))
