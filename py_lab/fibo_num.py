#!/usr/bin/python

N = int(input("fibonacci number? "))

count=0
a=0
b=0
c=1

while count<N:
	if(c==1) and (a==0):
		print("%d" %c,end=", ")
		a=c	
	elif (c==1) and (a==1):
		print("%d" %c,end=", ")
		b=c
		c=a+b
	elif (count==N-1):
		c=a+b
		a=b 
		print("%d" %c)
		b=c
	else:
		c=a+b
		a=b	
		print("%d" %c,end=", ")
		b=c	
	count += 1
print("F%d = %d" %(N, c))
