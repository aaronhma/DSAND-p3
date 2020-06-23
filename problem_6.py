import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    max_val = ints[0]
    min_val = ints[0]

    for i in ints:
        if i > max_val:
            max_val = i

        if i < min_val:
            min_val = i

    return (min_val, max_val)


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(17, 67)]
random.shuffle(l)

print("Pass" if ((17, 66) == get_min_max(l)) else "Fail")

# edge cases
l = [i for i in range(0, 1)]
random.shuffle(l)

print("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 0)]
random.shuffle(l)

print("Pass" if (None == get_min_max(l)) else "Fail")
