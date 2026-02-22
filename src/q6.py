def find_first_negative(lst):
    for num in lst:
      if num <0:
        return num
    return "No negatives"
    
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))