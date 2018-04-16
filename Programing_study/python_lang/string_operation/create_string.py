#!/usr/local/bin/python
#Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String 
string=raw_input("enter string:")
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
print(new)

