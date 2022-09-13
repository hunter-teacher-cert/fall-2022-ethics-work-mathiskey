# binsearch.py
# Shana Elizabeth Henry
# CSCI 77800 Fall 2022
# collaborators: Alex Long 


def binsearch(array, target):
    low = 0
    high = len(array) - 1
    mid = 0

    
    print (array[mid])
    while low < high:
        mid = (high + low) // 2
        if target < array[mid]:
              high = mid - 1
        elif target > array[mid]:
              low = mid + 1
        elif array[mid] == target:
            return mid
        print (high)
        print (mid)
        print (low)

    print (array[mid])

array = [1, 2, 3, 10, 30, 45, 60]
target = 45

print ("\n The target is at ", binsearch(array, target))




