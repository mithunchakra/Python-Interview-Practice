def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [8, 2, 14, 4, 6]

arr.sort()

target = int(input("Enter the target to be found: "))

result = binary_search(arr, target)

if result != -1:
    print("Found at index", result)
else:
    print("Not Found")