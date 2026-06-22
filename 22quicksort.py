"""
Interview Explanation

If the interviewer asks:

Explain Quick Sort.

Say:

Quick Sort selects a pivot element and partitions the remaining elements into two groups: elements smaller than or equal to the pivot and elements greater than the pivot. It recursively applies the same process to both groups and finally combines the sorted left part, pivot, and sorted right part.

Quick Visual Summary

Input:

[5,8,2,1,7]

Choose Pivot:

7

Partition:

Left  = [5,2,1]
Pivot = [7]
Right = [8]

Sort Left:

[1,2,5]

Combine:

[1,2,5] + [7] + [8]

=
[1,2,5,7,8]



"""

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for num in arr[:-1]:

        if num <= pivot:
            left.append(num)

        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = list(map(int, input("Enter numbers: ").split()))

print(quick_sort(arr))