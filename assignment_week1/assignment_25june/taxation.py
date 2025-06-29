print("Welcome to GlobalNext Tax Calculator")
print()

# ===== INPUT SECTION =====

# Name Input
while True:
    name = input("Enter Name: ").strip()
    if name != "" and len(name) <= 50:
        valid = True
        for ch in name:
            if not (ch.isalpha() or ch == ' '):
                valid = False
                break
        if valid:
            break
    print("Invalid name. Only alphabets and spaces allowed, max 50 characters.")

# Employee ID Input
while True:
    empid = input("Enter EmpID: ").strip()
    if len(empid) >= 5 and len(empid) <= 10:
        valid = True
        for ch in empid:
            if not (ch.isalnum()):
                valid = False
                break
        if valid:
            break
    print("Invalid EmpID. Must be alphanumeric and 5–10 characters.")

# Basic Monthly Salary Input
while True:
    value = input("Enter Basic Monthly Salary (₹): ").strip()
    try:
        basic_salary = float(value)
        if basic_salary >= 0 and basic_salary <= 10000000:
            break
    except:
        pass
    print("Invalid input. Salary must be between 0 and ₹1,00,00,000.")

# Special Allowance Input
while True:
    value = input("Enter Special Allowance (₹): ").strip()
    try:
        special_allowance = float(value)
        if special_allowance >= 0 and special_allowance <= 10000000:
            break
    except:
        pass
    print("Invalid input. Allowance must be between 0 and ₹1,00,00,000.")

# Bonus Percentage Input
while True:
    value = input("Enter Annual Bonus Percentage: ").strip()
    try:
        bonus_percent = float(value)
        if bonus_percent >= 0 and bonus_percent <= 100:
            break
    except:
        pass
    print("Invalid input. Bonus % must be between 0 and 100.")

# ===== CALCULATIONS =====

gross_monthly = basic_salary + special_allowance

if gross_monthly <= 0:
    print("Gross monthly salary must be greater than 0.")
    exit()

annual_bonus = gross_monthly * bonus_percent / 100
annual_gross = gross_monthly * 12 + annual_bonus

if annual_gross > 20000000:
    print("Annual gross salary exceeds realistic limit.")
    exit()

standard_deduction = 50000
taxable_income = annual_gross - standard_deduction
if taxable_income < 0:
    taxable_income = 0

# ===== TAX CALCULATION =====

slabs = [300000, 300000, 300000, 300000, 300000]
rates = [0.0, 0.05, 0.10, 0.15, 0.20, 0.30]

remaining = taxable_income
tax = 0
i = 0

while i < len(slabs):
    if remaining <= 0:
        break
    slab = slabs[i]
    if remaining > slab:
        tax += slab * rates[i]
        remaining -= slab
    else:
        tax += remaining * rates[i]
        remaining = 0
    i += 1

if remaining > 0:
    tax += remaining * rates[-1]

if taxable_income <= 700000:
    tax = 0

cess = tax * 0.04
total_tax = tax + cess
net_salary = annual_gross - total_tax

# ===== RUPEE FORMATTER (NO DEF) =====

# We'll use this code inline for each formatted output
# amount → string with ₹, comma and 2 decimal digits
def format_inline(amount):
    value = int(amount * 100 + 0.5)
    rupees = value // 100
    paise = value % 100

    s = ""
    count = 0
    if rupees == 0:
        s = "0"
    else:
        while rupees > 0:
            s = str(rupees % 10) + s
            rupees = rupees // 10
            count += 1
            if count > 3 and (count - 3) % 2 == 0 and rupees > 0:
                s = "," + s

    if paise < 10:
        paisa_str = "0" + str(paise)
    else:
        paisa_str = str(paise)

    return "₹" + s + "." + paisa_str

# ===== OUTPUT REPORT =====

print()
print("=" * 40)
print("EMPLOYEE TAX REPORT")
print("=" * 40)
print("Name:", name)
print("EmpID:", empid)
print("-" * 40)
print("Gross Monthly Salary :", format_inline(gross_monthly))
print("Annual Gross Salary  :", format_inline(annual_gross))
print("Standard Deduction   :", format_inline(standard_deduction))
print("Taxable Income       :", format_inline(taxable_income))
print("-" * 40)
print("Tax Before Cess      :", format_inline(tax))
print("Health + Edu Cess    :", format_inline(cess))
print("Total Tax Payable    :", format_inline(total_tax))
print("-" * 40)
print("Annual Net Salary    :", format_inline(net_salary))
print("=" * 40)
