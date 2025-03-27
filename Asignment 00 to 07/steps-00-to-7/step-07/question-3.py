def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

print(in_range(5, 1, 10))   # True (5 is between 1 and 10)
print(in_range(15, 1, 10))  # False (15 is greater than 10)
print(in_range(1, 1, 10))   # True (1 is equal to low)
print(in_range(10, 1, 10))  # True (10 is equal to high)
print(in_range(0, 1, 10))   # False (0 is less than 1)
