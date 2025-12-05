# Question 2
def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) 
      in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if the input is actually a list
    if not isinstance(lst, list):
        return "Error: The first argument must be a list."

    # Use list comprehension to create a new list with the replacements
    # Logic: Put 'replace_val' if the item matches, otherwise keep the 'item'
    modified_list = [replace_val if item == find_val else item for item in lst]
    
    return modified_list

# Task 2
# Invoke the function "find_and_replace" in:

# 1: [1, 2, 3, 4, 2, 2], 2, 5
result_1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(f"Scenario 1 Result: {result_1}")

# 2: ["apple", "banana", "apple"], "apple", "orange"
result_2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(f"Scenario 2 Result: {result_2}")
