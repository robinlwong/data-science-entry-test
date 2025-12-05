# Questiono 3
def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key is already in the dictionary
    if key in dct:
        print(f"Key '{key}' exists. Original value: {dct[key]}")
    
    # Update the dictionary (this works for both adding new keys and updating existing ones)
    dct[key] = value
    
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:

# Scenario 1: {}, "name", "Alice"
print("--- Scenario 1 ---")
result_1 = update_dictionary({}, "name", "Alice")
print(f"Result: {result_1}\n")

# Scenario 2: {"age": 25}, "age", 26
print("--- Scenario 2 ---")
result_2 = update_dictionary({"age": 25}, "age", 26)
print(f"Result: {result_2}")
