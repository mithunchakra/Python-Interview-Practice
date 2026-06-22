def secondlargest(arr):

    arr.sort() # Ascending order
    # arr.sort(reverse=True) --> For descending order

    return arr[-2]


arr = list(map(int, input("Enter the numbers: ").split()))

print("Second Largest:", secondlargest(arr))


print("--------------for smallest")

def secondsmallest(arr):

    arr.sort() # Ascending order
    # arr.sort(reverse=True) --> For descending order

    return arr[1]

print("Second smallest:", secondsmallest(arr))

