
from names_fun import *

print(responces[0])
print(responces[1])
print()
while True:
	txt=input("\nWrite Something with Space : ")
	for word in txt.split(' '):
		if word.upper() in comand.keys():
			try:
				comand[word.upper()]()
			except:
				print("Something is Wrong")
			finally:
				break
	else:
		sory()