#!/usr/bin/python

def O(n):
    o=oct(n)
    print("=> OCT> ", end = '')
    o=o.replace('0o','')
    print(o)

def D(n):
    s=str(n)
    print("=> DEC> "+s)

def H(n):
    h=hex(n)
    print("=> HEX> ", end='')
    h=h.replace('0x','')
    print(h.upper())

if __name__=='__main__':
    print("this is my_module...")

