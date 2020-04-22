#!/usr/bin/python
from my_pkg.conversion import *
from my_pkg.union_intersection import *

if __name__=='__main__':
	a=0
	while a!=3:
		a=int(input("Select menu: 1)conversion 2)union/intersection 3)exit? "))	
		if a==1:
			usr_input = int(input("input binary number: "),base=2)
			O(usr_input)
			D(usr_input)	
			H(usr_input)

		elif a==2:
			list1 = input("1st list: ")
			list2 = input("2nd list: ")
			u(list1, list2)
			i(list1, list2)
		
		elif a==3:
			print("exit the program..")

		else:
			print("wrong order...")

