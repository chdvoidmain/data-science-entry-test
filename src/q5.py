def check_divisibility(num, divisor):
    #if both number is not numeric return False
    if not (isinstance(num,int) and isinstance(divisor,int)):
      raise False    
    # If remainder is 0, it means divisible
    return num % divisor == 0


print(check_divisibility(10, 2))  # True
print(check_divisibility(7, 3))   # False