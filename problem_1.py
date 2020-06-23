def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number <= 2:
        return number

    low = 2
    high = number // 2

    while low <= high:
        mid = low + (high - low) // 2
        guess = mid * mid

        if guess == number:
            return mid
        elif guess < number:
            low = mid + 1
        else:
            high = mid - 1

    return high


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# edge cases
print("Pass" if (-1 == sqrt(-1)) else "Fail")
print("Pass" if (835 == sqrt(698354)) else "Fail")
print("Pass" if (-27 == sqrt(-27)) else "Fail")
