# Question 5
def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check for numeric inputs
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("Error: Inputs must be numeric.")
        return False
    
    # !Divide by 0
    if divisor == 0:
        print("Error: Cannot divide by zero.")
        return False

    # Return True if the remainder is 0, otherwise False
    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility":

# 1: 10, 2
# 10 divided by 2 is 5 with 0 remainder. Result should be True.
result_1 = check_divisibility(10, 2)
print(f"Is 10 divisible by 2? {result_1}")

# 2: 7, 3
# 7 divided by 3 is 2 with 1 remainder. Result should be False.
result_2 = check_divisibility(7, 3)
print(f"Is 7 divisible by 3?  {result_2}")