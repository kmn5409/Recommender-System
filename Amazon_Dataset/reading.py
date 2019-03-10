import json

#with open("metadata.json", "r") as f:
#	dict1 = json.load(f)
f = open("meta.csv","w+")
i= 0 
for line in open("metadata.json"):

	#print(line)
	#print(type(line))
	#for l in line:
	j = eval(line)
	if('price' not in list(j.keys())):
		continue
	'''
	if()
	if(i == 351 or i == 350):
		print(j)
		print(type(j))
		for key,value in j.items():
			print(key,value)
		print("\n\n")
	'''

	#print(i)
	#print(j["asin"])
	#print( j['price'] )
	#j = (eval(line))
	f.write("%s,%d\n" %(j["asin"],j["price"]))
	'''
	line = line.replace("\'","\"")
	#print(line)
	print(i)
	if(i == 5 or i == 4):
		print(line)
	try:
		j = json.loads(line)
	except NameError:
		continue
	else:
		continue

	#print(j["asin"])
	#print(j["asin"],j["price"])
	'''
	i+=1
	if(i%100000 == 0):
		print(i)
		#break

print("Here")
f.close()
