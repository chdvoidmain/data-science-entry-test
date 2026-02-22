def update_dictionary(dct, key, value):
    # check if key exists in dct dictionary
    if key in dct:
        # if yes print existing value
        print("Original value:", dct[key])
        # update key with new value
        dct[key] = value
    return dct


# Task 2
# Scenario 1
dct1 = {}
result1 = update_dictionary(dct1, "name", "Alice")
print(result1)

dct2 = {"age": 25}
# Scenario 2
result2 = update_dictionary(dct2, "age", 26)
print(result2)
