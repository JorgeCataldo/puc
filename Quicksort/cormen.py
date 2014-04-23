'''
Created on 19/04/2014

@author: cataldo
'''

QUICKSORT(A,p,r)
if p<r
    q=PARTITION(A,p,r)
    QUICKSORT(A,p,q-1)
    QUICKSORT(A,q+1,r)
    

PARTITION(A,p,r)
x=A[r]
i=p-1
for j=p to r-1
    if A[j]<=x
        i=i+1
        A[i] <=> A[j]
A[i+1] <=> A[r]
return 1+1




