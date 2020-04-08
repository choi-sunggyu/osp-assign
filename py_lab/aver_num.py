#!/usr/bin/python

N = int(input("How many number you input? ")) 
count=0
n=0
sum=0

while count<N:
	n = int(input("input: "))
	sum += n
	count += 1
aver=sum/N
print(aver)

	
