def string_reverse(s):
    result = ""
    # loop every characther in s
    for my_char in s:
        result = my_char + result  # append each character in the beginning of the string
    return result


# Task 2
print(string_reverse("Hello World"))
print(string_reverse("Python"))