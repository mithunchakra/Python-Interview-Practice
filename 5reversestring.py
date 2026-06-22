# using loop

def revstr(s):

    rev = ""

    for ch in s:
        rev = ch + rev

    return rev


s = input("Enter the string: ")

print(revstr(s))


# using slicing

def revstr(s):
    return s[::-1]

s = input("Enter the string: ")
print(revstr(s))