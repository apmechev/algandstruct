import pdb

def SortCount(A):
    """Outer mergesort helper function. 
    Accepts an array A.
    Output: Tuple of Sorted array A and number of inversions"""
    if len(A)<2 :
        return (A, 0)
    else:
        n=len(A)
        B ,x = SortCount(A[0:n/2])
        C ,y = SortCount(A[n/2:])
        D ,z = SortCountInv(B, C)
    return (D ,x+y+z)

def SortCountInv(A,B,):
    i,j=0,0
    s=0
    D=[]
    while i < len(A) and j<len(B) :
        if A[i] < B[j] :
            D.append(A[i])
            i+=1
        else:
            D.append(B[j])
            s+=len(A) -i 
            j+=1
    while i < len(A):
        D.append(A[i])
        i+=1
    while j < len(B):
        D.append(B[j])
        j+=1
    return D,s

