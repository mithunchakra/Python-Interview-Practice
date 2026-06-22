def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        print(f"{i}! = {fact}")

    return f"{fact} -- Is The final result"    

num = int(input("Enter the number"))
print(factorial(num))        
