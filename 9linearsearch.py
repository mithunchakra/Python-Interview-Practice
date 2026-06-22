arr = [10, 20, 30, 40]

key = int(input("Enter key: "))

for i in range(len(arr)):

    if arr[i] == key:
        print("Found at index", i)
        break

else:
    print("Not Found")