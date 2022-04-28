import numpy as np
from numpy import random


def counting_Sort(array):
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


def inserection_Sort(array): #input array not ordened A[0...(len(A) -1)]
    n = len(array)
    for i in range(1,n):  #for from 1 to len(A) -1
        key = array[i]
        j = i - 1
        while (j > -1 and array[j] > key): #search for the right position for the positioning of the key
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key   #inserection of key in the sub array of length j = i-1
    return array

def new_array(l):
    array = [0 for i in range(l)] 
    for x in range(len(array)):
        array[x] = int(random.randint(1, l))
    print(str(array) + 'array')
    return array

def presence_search(array, n, i, f): #array is ordened
    if i <= f:
        pivot = round((f+i)/2)

        #looking in the positions prior to the pivot
        if array[pivot] > n:
            return presence_search(array,n,i,pivot - 1)

        #looking in the positions following the pivot
        if array[pivot] < n:
            return presence_search(array,n,pivot + 1,f)

        #n founded
        if array[pivot] == n:
            return 'Number ' + str(n) + ' in ' + str(pivot) + '° position '
    #n not fonded
    if i > f:
        return 'ERROR ' + str(n) + ' NOT FOUND'



def presence_search2(array,n): #only 2 parameters and array ordered
    l = len(array)
    if l >= 1:
        pivot = round(l/2)

        #looking in the positions prior to the pivot
        if array[pivot] > n: 
            return presence_search2(array[0:pivot],n)

        #looking in the positions following the pivot
        if array[pivot] < n: 
            return presence_search2(array[pivot+1:l-1],n)

        #n founded
        if array[pivot] == n: #n founded
            return 'Number ' + str(n) + ' in ' + str(pivot) + '° position '
    
    #n not fonded
    else: 
        return 'ERROR ' + str(n) + ' NOT FOUND'


def radix_sort(array):
    d = len(str(max(array))) #number of max array's digits
    digits = [[] for i in range(d)]
    for i in range(len(array)): #to see all array's elements
        for j in range(d+1): #to divide alla array's elements in how many digits they have
            if len(str(array[i])) == j:
                digits[j-1].append(array[i])
    
    for i in range(d): # ordined algoritms of every 'digits'
        digits[i] = inserection_Sort(digits[i])
        if i == 0:
            nA = digits[0]
        else:
            nA += digits[i]
    return nA



#print(counting_Sort(new_array(5)))  #no zeros
#print(bubble_Sort(new_array(10)))
#print(inserection_Sort(new_array(10)))
#arr = [1,2,3,4,4,4,5,5,7,8,9,22,22,33,45,67]
#print(presence_search(arr,5,0,16))
#print(presence_search2(arr,5))
#print(radix_sort(new_array(200)))