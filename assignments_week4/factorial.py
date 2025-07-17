#Factorial Calculation
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number value which u want to find factorial : "))
print(factorial(n))