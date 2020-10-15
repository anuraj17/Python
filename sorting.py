"""
Sorting a list of numbers in ascending order
"""
import random

#Data Generator
randomData = []
for i in range(0, 7):
    randomData.append(random.randint(0, 50))

#Printer Function
def printOutput(data):
    print(data)

#Verify Sorting
def Verify(data):
    
    print("Result Data:")
    printOutput(data)

    for i in range(0, len(data) - 1):
        if(data[i] > data[i + 1]):
            print("Sorting Failed")
            exit(0)
    print("Sorting Successfull")

algorithmSelector = 3

#********************************1: QUICKSORT BEGINS***************************************************
"""
QuickSort:
Choose the last element as the Pivot recursively
Advantages:
Disadvantages:
Time Complexity:
Space Complexity:
"""
def quickSort(data, low, high):
    if(low < high):
        pi = quickSortPartition(data, low, high)
        quickSort(data, low, pi - 1)
        quickSort(data, pi + 1, high)

def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    return data

def quickSortPartition(data, low, high):
    pivot = data[high]

    i = low - 1

    for k in range(low, high):
        if(data[k] < pivot):
            i = i + 1
            swap(data, i, k)
    
    swap(data, i + 1, high)
    return i + 1

if (algorithmSelector == 1):
    print("Random Data")
    printOutput(randomData)
    quickSortData = list(randomData)
    quickSort(quickSortData, 0, len(quickSortData) - 1)
    Verify(quickSortData)
#*********************************QUICKSORT ENDS*******************************************************

#********************************2: MERGESORT BEGINS***************************************************
"""
MergeSort:
Split till there is only one element, and then sort while combining them back
Advantages:
Disadvantages:
Time Complexity:
Space Complexity:
"""

def mergeSort(data):
    if(len(data) > 1):

        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                data[k] = left[i]
                i = i + 1
            
            else:
                data[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            data[k] = left[i]
            k = k + 1
            i = i + 1

        while j < len(right):
            data[k] = right[j]
            k = k + 1
            j = j + 1   
        
if (algorithmSelector == 2):
    print("Random Data")
    printOutput(randomData)
    mergeSortData = list(randomData)
    mergeSort(mergeSortData)
    Verify(mergeSortData)
#********************************MERGESORT ENDS***************************************************

#********************************3: QUICKSORT BEGINS***************************************************
"""
InsertionSort:
Compare every element with its preceding element
Advantages:
Disadvantages:
Time Complexity:
Space Complexity:
"""
def insertionSort(data):

    for i in range(0, len(data) - 1):
        j = i + 1
        while j > 0:

            print(j)
            if(data[j] < data[j - 1]):
                swap(data, j - 1, j)
            print(data)
            j = j - 1

        
if (algorithmSelector == 3):
    print("Random Data")
    printOutput(randomData)
    insertionSortData = list(randomData)
    insertionSort(insertionSortData)
    Verify(insertionSortData)

#********************************QUICKSORT ENDS***************************************************