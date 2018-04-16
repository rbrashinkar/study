#!/usr/local/bin/python
#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String 
str1=raw_input("enter the string:")
count=0
count1=0
for i in str1:
  if(i.islower()):
     count=count+1
  elif(i.isupper()):
     count1=count1+1
print("lowercase letter is:")
print(count)
print("uppercase letter is:")
print(count1)
