"""Bubble sort algorithm in different variations"""


def bubble_sort(input_list: list, reverse: bool=False) -> None:
    """Performs a bubble sort on a given input list

    :param input_list: List to be sorted
    :type input_list: list
    :param reverse: Reverses sorted order
    :type reverse: bool
    :return: None
    """
    has_swapped = True
    while has_swapped:
        has_swapped = False

        for i in range(0, len(input_list) - 1):
            if reverse:
                if input_list[i] < input_list[i+1]:
                    input_list[i], input_list[i+1] = (
                        input_list[i+1], input_list[i]
                    )
                    has_swapped = True
            else:
                if input_list[i] > input_list[i+1]:
                    input_list[i], input_list[i+1] = (
                        input_list[i+1], input_list[i]
                    )
                    has_swapped = True


def bubble_sort_2(input_list: list, reverse: bool=False) -> None:
    """Performs a bubble sort on a given input list

    :param input_list: List to be sorted
    :type input_list: list
    :param reverse: Reverses sorted order
    :type reverse: bool
    :return: None
    """

    for i in range(0, len(input_list)):
        for j in range(i, len(input_list)):
            if reverse:
                if input_list[i] < input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
            else:
                if input_list[i] > input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
