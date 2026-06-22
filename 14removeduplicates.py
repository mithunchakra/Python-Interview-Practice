# Easy method

arr = [1, 2, 2, 3, 4, 4, 5]

result = list(set(arr))

print(result)


print("----------------------->")

# using loop

def remove_duplicates(arr):

    result = []

    for num in arr:

        if num not in result:
            result.append(num)

    return result


arr = list(map(int, input("Enter numbers: ").split()))

print(remove_duplicates(arr))