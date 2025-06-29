#Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
n = int(input('Enter N (term) value: '))
m = int(input('Enter number of terms: '))

sum_of_series = 0
sign = -1
for i in range(m):
    numerator   = n ** 2 ** i
    dinominator = 2 * i + 1
    sign        = -1 * sign
    term        = numerator / dinominator * sign
    sum_of_series += term
print(f"The sum of series of {m} terms is ",sum_of_series)