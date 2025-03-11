n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print(f"The factorial of {n} is: {fact}")
