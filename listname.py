wholename = []
firstname = []
lastname  = []

with open("classNames.txt") as listname:
	for name in listname:
		name = name.replace("\n", "")
		wholename.append(name)
		eachname = name.split()
		firstname.append(eachname[0])
		lastname.append(eachname[1])
	print wholename	
	print firstname
	print lastname

