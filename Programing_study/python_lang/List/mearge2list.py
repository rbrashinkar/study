#!/usr/local/bin/python
#Python Program to Merge Two Lists and Sort it
a=[]
c=[]
d=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
print(a)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    b=int(input("Enter element:"))
    c.append(b)
print(c)
print("merged list is:")
#d.append(a+c)
d=a+c
d.sort()
print(d)
