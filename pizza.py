
def pizzacost(pizzaradius, slidecost):

	pizzaradius = input('Please enter your pizza radius: ')
    slidecost = input('Please enter the cost of your pizza slide: ')

	if(pizzaradius =< 6 ):
		cost = pizzacost * 4
	elif(pizzaradius > 6 ):
		cost = pizzacost * 8
	print('Pizza cost: ', cost)
	