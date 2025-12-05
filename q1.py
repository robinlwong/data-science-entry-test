# Question 1
def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
# Check if both x and y are numbers (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values without a temporary variable
    x, y = y, x
    
    print(f"Swapped: x is now {x}, y is now {y}")
    return

# Task 2
# Invoke the function "swap":

# 1: "Apple", 10
# We print the result to see the return value because the function returns -1 here
result_1 = swap("Apple", 10)
print(f"Result for ('Apple', 10): {result_1}") 

# 2: 9, 17
print("Result for (9, 17):")
swap(9, 17)