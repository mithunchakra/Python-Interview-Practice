num = int(input())

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

if original == sum:
    print("Armstrong")
else:
    print("Not Armstrong")