ages={"sh":62,"rt":34,"yy":55,"tyy":44}
young_person = None
currentsmall=1000
for name in ages:
	
	age =ages[name]
	if age<currentsmall:
		young_person = name
		currentsmall=age
print(young_person)

