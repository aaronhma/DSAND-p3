def sort_012(arr: list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low, high, current = 0, len(arr) - 1, 0

    while current <= high:
        if arr[current] == 0:
            temp = arr[current]
            arr[current] = arr[low]
            arr[low] = temp

            low += 1
            current += 1

        elif arr[current] == 2:
            temp = arr[current]
            arr[current] = arr[high]
            arr[high] = temp

            high -= 1

        else:
            current += 1

    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 0, 2, 1, 1, 0])
test_function([])
test_function(["temp"])
