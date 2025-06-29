#2. Print N Fibo terms with 1 and 2 as 1st 2 terms.
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
terms = int(input("Enter the total number of terms : "))
print(f"The fibonacci series of {terms} terms  is :")
for i in range (1, terms+1):
    print(fibonacci(i),end =" ")