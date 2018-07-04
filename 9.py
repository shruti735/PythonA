def decision(age):
	if person_is_old(age):
		print("You deserve a vacation")
	else:
		print("Go to work")
def person_is_old(age):
	if age > 60:
		return True
	else:
		return False
decision(20)
