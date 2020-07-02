responces=["Welcome to Name Related Works","My Name is Nastiya","Thank You for Used Me"]

def sort_form_name():
	str=""
	name=input("Enter Your Name : ")
	for later in name.split(' '):
		str+=(later[0:1:])#store first later in words
	for i in str:
		print(i,end=".")#print fist later of stored string one by one with dot seprate no line change

def reverse_name():
	str=""
	name=input("Enter Your Name : ")
	str+=name[-1::-1]
	print(str)


def first_name():
	l=[]
	name=input("Enter Your Name : ")
	for later in name.split(' '):
		l.append(later)
	print(l[0])

def middle_name():
	l=[]
	name=input("Enter Your Name : ")
	for later in name.split(' '):
		l.append(later)
	print(l[1])

def last_name():
	l=[]
	name=input("Enter Your Name : ")
	for later in name.split(' '):
		l.append(later)
	print(l[3])
	
def total_name():
	l=[]
	name=input("Enter Your Name : ")
	for later in name.split(' '):
		l.append(later)
	for i in l:
		print(i,end=" ")

def nastiya():
	print("Hello!")
def end():
	input("Press any key to Exit")
	print(responces[2])
	exit()

def myname():
	print(responces[1])
	
def sory():
	print("Beyond My Ability")

def clear():
	import os
	os.system("cls")

comand={"SORT":sort_form_name,"S NAME":sort_form_name,"REVERSE":reverse_name,"FIRST":first_name,"SECOND":middle_name,"MIDLE":middle_name,"MIDDLE":middle_name,"LAST":last_name,"THIRD":last_name,"TOTAL":total_name,"COMPLETE":total_name,"END":end,"EXIT":end,"NAME":myname,"CLEAR":clear,"CLS":clear,"NASTIYA":nastiya}