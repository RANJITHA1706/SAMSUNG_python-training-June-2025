'''7. Print the following shapes by accepting number of lines
A. Right Angled Triangle
B. Equi lateral Triangle
C. Hollow Square
D. Howllow Rhombus
E. Pascal's Triangle
F. X shape
G. X shape inside hollow Square with 0 at middle/center
H. Benzene Ring (C6H6) Hexagon '''


number_of_lines = int(input("Enter the number of lines : "))
print("1 .Right Angled Triangle")
for i in range(1,number_of_lines+1):
    print("#  " * i)

print("2 .Equi lateral Triangle")
for i in range(number_of_lines):
    print(" " * (number_of_lines-i-1) + "* " * (i+1))

print("3. Hollow Square")
for i in range(number_of_lines):
    for j in range(number_of_lines):
        if i == 0 or i == number_of_lines-1 or j == 0 or j == number_of_lines-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
print("4.Hollow rhombus")
for i in range(number_of_lines):
    print(" " * (number_of_lines-i-1), end="")
    for j in range(number_of_lines):
        if i == 0 or i == number_of_lines-1 or j == 0 or j == number_of_lines-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


print("5.Pascal's Triangle")
for i in range(number_of_lines):
    print(" " * (number_of_lines - i), end="")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
print("6.X Shape ")
for i in range(number_of_lines):
    for j in range(number_of_lines):
        if i == j or i + j == number_of_lines - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("7.X shape inside hollow Square with 0 at middle/center")
for i in range(number_of_lines):
    for j in range(number_of_lines):
        if (i == 0 or i == number_of_lines-1 or j == 0 or j == number_of_lines-1 or i == j or i + j == number_of_lines - 1):
            if i == j == number_of_lines // 2:
                print("0", end="")
            else:
                print("*", end="")
        else:
            print(" ", end="")
    print()
print("8.Benzene Ring (C6H6) Hexagon")
n = 5
print(" " * 4 + " _____")
print(" " * 3 + "/     \\")
print(" " * 2 + "/  C6  \\")
print(" " * 2 + "\\  H6  /")
print(" " * 3 + "\\_____/")






