from itertools import permutations
digit=[0,1,2,3,4,5,6,7,8,9]
perm=[]
perm =permutations(digit)
for i in range(perm):
         if(len(i)==2):
             print i
