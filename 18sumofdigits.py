num = int(input())

total = 0

while num:
    total += num % 10
    num //= 10

print(total)

# Total numbers sum in array

arr = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in arr:
    total += num

print(total)

# To print sum 1 to n

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(total)


# To find sum of even number

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):

    if i % 2 == 0:
        total += i

print(total)