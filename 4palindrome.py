#Reversing a number
def reverse_number(n):

    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev

num = int(input("Enter a number: "))
print(reverse_number(num))






# For a single number

def palindrome(n):

    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if original == rev:
        print(f"{original} --> Palindrome")
    else:
        print(f"{original} --> Not Palindrome")


num = int(input("Enter a number: "))
palindrome(num)




print("-------------------------------------------------->")
# For multiple numbers in a list
def palindrome(n):

    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if original == rev:
        print(f"{original} --> Palindrome")
    else:
        print(f"{original} --> Not Palindrome")


nums = list(map(int, input("Enter numbers: ").split()))

for num in nums:
    palindrome(num)



# Using for strings
print("--------------> Strings")

def palindrome(s):

    if s == s[::-1]:
        print(f"{s} --> Palindrome")
    else:
        print(f"{s} --> Not Palindrome")

s = input("Enter a string: ")
palindrome(s)


# For multiple strings

def palindrome(s):

    if s == s[::-1]:
        print(f"{s} --> Palindrome")
    else:
        print(f"{s} --> Not Palindrome")


strings = input("Enter strings separated by space: ").split()

for s in strings:
    palindrome(s)