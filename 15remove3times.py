arr = list(map(int, input("Enter numbers: ").split()))

result = []

for num in arr:

    if result.count(num) < 2:  # for removing duplicate just use    if result.count(num) < 1:
        result.append(num)

print(result)


# To print number occcuring more than once

arr = list(map(int, input("Enter numbers: ").split()))

result = []

for num in arr:

    if arr.count(num) > 1 and num not in result:
        result.append(num)

print(result)