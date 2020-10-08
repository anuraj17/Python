"""
Sorting a list of numbers in ascending order
"""
import random

#Data Generator
randomData = []
for i in range(0, 20):
    randomData.append(random.randint(0, 50))
print("Random Data")
print(randomData)

#Printer Function
def printOutput(data):
    print("\nSorted Data")
    print(data)

#Verify Sorting
def Verify(arr):
    for i in range(0, len(arr) - 1):
        if(arr[i] > arr[i + 1]):
            print("Sorting Failed")
            exit(0)
    print("Sorting Successfull")

"""
QuickSort:
Choose the last element as the Partition recursively
"""
def quickSort(arr, low, high):
    if(low < high):
        pi = quickSortPartition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def quickSortPartition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for k in range(low, high):
        if(arr[k] < pivot):
            i = i + 1
            swap(arr, i, k)
    
    swap(arr, i + 1, high)
    return i + 1

quickSort(randomData, 0, len(randomData) - 1)
printOutput(randomData)
Verify(randomData)
