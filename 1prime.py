nums = list(map(int, input("Enter the numbers:").split()))

for num in nums:

  if num <= 1:
    print("Not Prime")

  else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break;
    
    if is_prime:
        print(f"{num} --> Prime Number")

    else:
        print(f"{num} --> Not a prime number")    