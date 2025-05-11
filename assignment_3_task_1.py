n=int(input("Enter a Number: "))
def factorial(n):
    if n<0:
        print("Factorial is not defined for negative numbers")
    elif n==0:
        return 1
    else:
        fact=1
        for i in range(1, n+1):
            fact=fact * i
        return fact
result= factorial(n)
print("factorial of", n, "is", result)

