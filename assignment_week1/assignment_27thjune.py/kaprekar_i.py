# Kaprekar's Constant (6174)
num = input("Enter a 4-digit number: ")
count = 0

if len(num) != 4 or not num.isdigit():
    print("Invalid input")
else:
    while num != "6174":
        digits = []
        for ch in num:
            digits.append(int(ch))

        while len(digits) < 4:
            digits.append(0)

        for i in range(3):
            for j in range(i+1, 4):
                if digits[i] > digits[j]:
                    digits[i], digits[j] = digits[j], digits[i]

        asc = digits[0]*1000 + digits[1]*100 + digits[2]*10 + digits[3]
        desc = digits[3]*1000 + digits[2]*100 + digits[1]*10 + digits[0]

        result = desc - asc
        num = str(result)
        if len(num) == 1:
            num = "000" + num
        elif len(num) == 2:
            num = "00" + num
        elif len(num) == 3:
            num = "0" + num

        count += 1

        if num == "0000":
            break  # All digits same

    if num == "6174":
        print("Reached 6174 in", count, "steps.")
    else:
        print("Kaprekar process stuck. All digits same.")
