from itertools import permutations


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    t = str(input_list)

    perm = permutations(t)

    perm = list(perm)

    for i in perm:
        i = int(i)
        print("value: ", i)

    max_1 = max(perm)
    perm.remove(max_1)
    max_2 = max(perm)

    return [max_1, max_2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
