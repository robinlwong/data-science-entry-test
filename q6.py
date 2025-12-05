# Question 6
def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Initialize index variable
    i = 0
    
    # Loop runs as long as the index is smaller than the list length
    while i < len(lst):
        # Check if the current element is negative
        if lst[i] < 0:
            return lst[i]  # Return immediately when found
        
        # Increment index
        i += 1
        
    # If the loop finishes without returning, no negatives were found
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative":

# 1: [3, 5, -1, 7, -2, 8]
# Should return -1 (stops at the first negative)
result_1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(f"Result 1: {result_1}")

# 2: [2, 10, 7, 0]
# Should return "No negatives"
result_2 = find_first_negative([2, 10, 7, 0])
print(f"Result 2: {result_2}")