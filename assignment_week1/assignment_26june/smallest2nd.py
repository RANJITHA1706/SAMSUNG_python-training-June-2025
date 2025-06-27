#Find 2nd smallest digit in a number
number = int(input("Enter the digit:"))
digit_list = list(str(number))
digit_list.sort()
if len(digit_list) < 2:
    print("Cannot find the second smallest")
else:
    print("The second smallest digit in the number", digit_list[1])