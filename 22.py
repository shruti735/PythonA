ages={"sh":12,"rt":34,"yy":55,"tyy":44}
oldest_person = None
currentbig=0
for name in ages:
	age =ages[name]
	if age>currentbig:
		oldest_person = name
		currentbig=age
print(oldest_person)
	

