def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) <= 1:
        return -1

    def findPivot(arr: list):
        low = 0
        high = len(arr) - 1

        if arr[low] < arr[high]:
            return 0

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] > arr[mid + 1]:
                return mid + 1
            elif arr[mid] < arr[low]:
                high = mid - 1
            else:
                low = mid + 1

        return high

    def search(arr: list, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            guess = arr[mid]

            if (guess == target):
                return mid
            elif (guess < target):
                low = mid + 1
            else:
                high = mid - 1

        return -1

    pivot = findPivot(input_list)
    s1 = search(input_list[:pivot], number)
    s2 = search(input_list[pivot:], number)

    if s1 != -1:
        return s1
    elif s2 != -1:
        return s2 + pivot
    else:
        return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([["test", "udacity"], "udacity"])
test_function([["test", "udacity"], "test"])
test_function([["test"], "udacity"])
