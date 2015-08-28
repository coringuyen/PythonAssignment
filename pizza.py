
def pizzacost(pizzaradius, slidecost):

	if(pizzaradius <= 6):
		cost = slidecost * 4
	elif(pizzaradius > 6 ):
		cost = slidecost * 8
	print "Pizza cost: $", cost
	
pizzaradius = input('Please enter your pizza radius: ')
slidecost = input('Please enter the cost of your pizza slide: ')
pizzacost(pizzaradius, slidecost)