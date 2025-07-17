#Generate Parantheses
def generate_parentheses(n):
    def backtrack(s, open_count, close_count):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open_count < n:
            backtrack(s + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(s + ')', open_count, close_count + 1)

    result = []
    backtrack("", 0, 0)
    return result

try:
    n = int(input("Enter the number of pairs of parentheses: "))
    if n < 0:
        raise ValueError
    combinations = generate_parentheses(n)
    print(f"\n Found {len(combinations)} valid combinations:")
    for idx, comb in enumerate(combinations, 1):
        print(f"{idx}. {comb}")
except ValueError:
    print("Please enter a valid non-negative integer.")
