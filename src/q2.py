def find_and_replace(lst, find_val, replace_val):
    print("Original lst ",lst)
    print("find_val ", find_val)
    print("replace_val ", replace_val)
    if not isinstance(lst, list):
        print("lst is NOT a list")
        return -1
    
    # for loop entire lst items
    for i in range(len(lst)):
        # if found then replace find_val variable with replace_val variable
        if lst[i] == find_val:
            lst[i] = replace_val
    # return updated lst
    print("Updated lst ",lst)
    return lst

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))