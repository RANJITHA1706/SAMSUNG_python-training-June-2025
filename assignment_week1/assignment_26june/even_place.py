number = int(input("Enter the number : "))
digit = list(str(number))
digit_length = len(digit)
even_sum = 0
for i in range(0,digit_length,2):
    even_sum += int(digit[i])

print("The sum of even place digit is ", even_sum)