# get nth number of Fibnocci sequence 
# assuming only positive numbers

def fibnocci(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	elif x > 1:
		return fibnocci2(x-1) + fibnocci2(x-2)
		
print fibnocci2(6)
