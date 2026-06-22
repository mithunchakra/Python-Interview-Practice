num = int(input())

count = 0

while num:
    count += 1
    num //= 10

print(count)