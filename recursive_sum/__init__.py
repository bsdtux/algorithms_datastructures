"""Recusively sum a list of number"""


def recursive_sum(input_list: list) -> int:
    """Recursively sum a list of integers

    :param input_list: List to sum
    :type input_list: list
    :return: int
    """
    if len(input_list) == 0:
        return 0

    return input_list.pop() + recursive_sum(input_list)


def recursive_sum_2(input_list: list) -> int:
    """Recursively sum a list of integers

    :param input_list: List to sum
    :type input_list: list
    :return: int
    """
    if len(input_list) == 0:
        return 0
    else:
        current = input_list[0]
        return current + recursive_sum(input_list[1:])
