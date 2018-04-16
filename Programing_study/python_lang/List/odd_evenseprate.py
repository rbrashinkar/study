#!/user/local/bin/python
#Python Program to Put Even and Odd elements in a List into Two Different Lists 
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
odd=[]
even=[]
for i in a:
    if(i%2==0):
      even.append(i)
    else:
      odd.append(i)

print(even)
print(odd)
