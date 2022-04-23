import numpy as np
from numpy import random


def counting_Sort(array):
    print(int(max(array)))
    counting = [0 for i in range(max(array) + 1)] 
    for x in array: #counting the occorrency
        counting[x] +=1
    k = len(array) - 1
    for i in range(int(max(array)),0, -1): #making the new ordened array
            while (counting[i] != 0):
                array[k] = i
                counting[i] -=1
                k -=1
    return array
        
         

    
def bubble_Sort(arr):
    n = len(arr) # Traverse through all array elements
    for i in range(n-1): # range(n) also work but outer loop will # repeat one time more than needed. # Last i elements are already in place
        for j in range(0, n-i-1): # traverse the array from 0 to n-i-1 # Swap if the element found is greater # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

        

def new_array(l):
    array = [0 for i in range(l)] 
    for x in range(len(array)):
        array[x] = int(random.randint(1, l))
    print(str(array) + 'array')
    return array



print(counting_Sort(new_array(5)))  #no zeros
print(bubble_Sort(new_array(10)))