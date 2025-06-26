#Find sum of the Odd placed Even digits in the given number.
number = int(input("Enter the number : "))
digit = list(str(number))
digit_length = len(digit)
odd_sum = 0
for i in range(1,digit_length,2):
    odd_sum += int(digit[i])

print("The sum of odd place digit is ", odd_sum)