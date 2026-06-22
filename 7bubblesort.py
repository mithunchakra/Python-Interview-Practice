'''
Bubble Sort is a simple sorting algorithm that repeatedly 
compares adjacent elements and swaps them if they are in the wrong order. After each pass,
 the largest element "bubbles up" to its correct position at the end of the list.

'''

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


nums = [5, 3, 8, 4, 2]

print(bubble_sort(nums))



print("-----------------------------------> next type")
''' For multiple'''

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


nums = list(map(int, input("Enter numbers: ").split()))

print(bubble_sort(nums))

