# Shortcut method

arr = [10, 50, 20, 40, 30]

arr.sort()

print(arr[-1])



print("-------------------------------------------------------> Long method")





def Largest(arr):

    largest = arr[0]
    index = 0

    for i in range(len(arr)):

        if arr[i] > largest:
            largest = arr[i]
            index = i

    return f"{largest} --> Found at index {index}"


arr = list(map(int, input("Enter the numbers: ").split()))

print(Largest(arr))

print("----------------------------------------> For smallest integer")

def smallest(arr):

    small = arr[0]

    for i in arr:
        if i < small:
            small = i

    return small

print(smallest(arr))