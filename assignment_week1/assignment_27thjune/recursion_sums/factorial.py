def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number *factorial(number-1)
num =int(input("Enter the number you want to find factorial : "))
print(f"Factorial of {num} is ",factorial(num))    
