#!/usr/bin/python

def u(a,b):
	list1=[]
	list2=[]

	a=a.replace(' ','')
	a=a.replace('[','')
	a=a.replace(']','')
	a=a.split(',')
	for member in a:
		list1.append(int(member))

	b=b.replace(' ','')
	b=b.replace('[','')
	b=b.replace(']','')
	b=b.split(',')
	for member in b:
		list2.append(int(member)) 

	list3=list(set(list1).union(set(list2)))
	print("=> union ", end = '')
	print(list3)

def i(a,b):
	list1=[]
	list2=[]

	a=a.replace(' ','')
	a=a.replace('[','')
	a=a.replace(']','')
	a=a.split(',')
	for member in a:
		list1.append(int(member))       

	b=b.replace(' ','')
	b=b.replace('[','')
	b=b.replace(']','')
	b=b.split(',')
	for member in b:
		list2.append(int(member))

	list3=list(set(list1).intersection(set(list2)))
	print("=> intersection ", end='')
	print(list3)

if __name__=='__main__':
    print("this is my_module...")

