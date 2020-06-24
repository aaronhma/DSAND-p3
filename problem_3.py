def merge(left_list, right_list):
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            merged_list.append(right_list[right_index])
            right_index += 1
        else:
            merged_list.append(left_list[left_index])
            left_index += 1

    merged_list += left_list[left_index:]
    merged_list += right_list[right_index:]

    return merged_list


def sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid_index = len(input_list) // 2
    left_list = sort(input_list[0:mid_index])
    right_list = sort(input_list[mid_index:])

    return merge(left_list, right_list)


def rearrange_digits(input_list):
    """
    Extract two numbers from the given array, whose sum is the maximum value possible using the available digits
    :param input_list: list
    :return: tuple
    """
    if len(input_list) <= 1:
        return [-1]

    sorted_list = sort(input_list)
    number_one_list = [str(x) for x in sorted_list[0::2] if x >= 0]
    number_two_list = [str(x) for x in sorted_list[1::2] if x >= 0]

    return int(''.join(number_one_list)), int(''.join(number_two_list))


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], [-1]])
test_function([[0, 1], [1, 0]])
test_function([[0, 0], [0, 0]])
