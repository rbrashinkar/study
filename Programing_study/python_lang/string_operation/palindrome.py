#!/usr/local/bin/python
#Python Program to Check if a String is a Palindrome or Not 
str1=raw_input("enter the string:")
str2=str1[::-1]
print(str1)
print(str2)
if(str1==str2):
  print("string is palindrome")
else:
  print("string is not palindrome")
