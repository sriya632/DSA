'''Problem statement
Ninja has been given two sorted arrays/lists, ‘ARR1’ and ‘ARR2’ of lengths ‘M’ and ‘N’ respectively. He is also provided with an integer ‘K’. He has to find the ‘K’th element (1 based indexing) in the sorted array/list of length ‘M + N’ made by merging ‘ARR1’ and ‘ARR2’.
For example :
‘ARR1’ = {1, 4, 6, 7} 
‘ARR2’ = {2, 3, 5, 6} 
‘K’ = 6

So the sorted array after merging ‘ARR1’ and ‘ARR2’ will be:
{1, 2, 3, 4, 5, 6, 6, 7}
So the 6th element (1 based indexing) is in the new sorted merged array/list is 6.
As Ninja is busy with the preparation of his upcoming exams so, he asks you for help. Can you help Ninja to solve this problem?
Follow Up :
Try to do this problem without using any extra space.'''

from os import *
from sys import *
from collections import *
from math import *

def findKthElement(arr1, arr2, k):
    '''arr=arr1+arr2
    arr.sort() - uses extra space'''
    m, n = len(arr1), len(arr2)

    if m == 0:
        return arr2[k - 1]
    if n == 0:
        return arr1[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])
    
    i = min(m, k // 2)
    j = min(n, k // 2)

    if arr1[i - 1] < arr2[j - 1]:
        return findKthElement(arr1[i:], arr2, k - i)
    else:
        return findKthElement(arr1, arr2[j:], k - j)

def main():
    arr1 = [1, 4, 6, 7]
    arr2 = [2, 3, 5, 6]
    k = 6
    print(findKthElement(arr1, arr2, k))
    
if __name__ == "__main__":
    main()