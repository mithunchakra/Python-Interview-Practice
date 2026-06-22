s = input().lower()

count = 0

for ch in s:
    if ch in "aeiou":
        print(ch, end=" ")
        count += 1

print("\nTotal vowels:", count)