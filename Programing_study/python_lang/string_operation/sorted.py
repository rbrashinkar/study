#!/usr/local/bin/python
#Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically 
#strng=raw_input("Enter string:")
print("Enter a hyphen separated sequence of words:")
lst=[n for n in raw_input().split('-')]  
lst.sort()
print("Sorted:")
print('-'.join(lst))


