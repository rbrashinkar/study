#!/usr/local/bin/python
str1=raw_input("enter string:")
count=0
count1=0
for i in str1:
  if(i.isdigit()):
     count=count+1
  count1=count1+1
print("The number of digits is:")
print(count)
print("The number of characters is:")
print(count1)
