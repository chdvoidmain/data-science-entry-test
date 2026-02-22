def swap(x, y):
    # Check if both x and y are numeric, numeric in python my assumptions is int and float
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("x or y are NOT numeric. return -1")
        return -1
    else:
        print("Both numbers are numeric. Good to go.")
    
    # Swap without additional temporary variable
    x = x + y
    y = x - y
    x = x - y
    
    print("Swapped values:")
    print("x =", x)
    print("y =", y)

print(swap("Apple", 10))  # Should return -1 - negative scenario
swap(9, 17)               # Should print swapped values - positive scenario