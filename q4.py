# Question 4
def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if the input is actually a string
    if not isinstance(s, str):
        return "Error: Input must be a string."
    
    # Use string slicing with a step of -1 to reverse it
    return s[::-1]

# Task 2
# Invoke the function "string_reverse":

# 1: "Hello World"
result_1 = string_reverse("Hello World")
print(f"Original: 'Hello World' | Reversed: '{result_1}'")

# 2: "Python"
result_2 = string_reverse("Python")
print(f"Original: 'Python'      | Reversed: '{result_2}'")