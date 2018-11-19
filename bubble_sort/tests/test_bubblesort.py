from bubble_sort import bubble_sort, bubble_sort_2


def test_bubble_sort():
    unsorted = []
    expected = []

    bubble_sort(unsorted)
    assert expected == unsorted

    unsorted = [2, 1, 3]
    expected = [1, 2, 3]

    bubble_sort(unsorted)

    assert expected == unsorted


def test_bubble_sort_reversed():
    unsorted = []
    expected = []

    bubble_sort(unsorted, True)
    assert expected == unsorted

    unsorted = [2, 1, 3]
    expected = [3, 2, 1]

    bubble_sort(unsorted, True)

    assert expected == unsorted


def test_bubble_sort_2():
    unsorted = []
    expected = []

    bubble_sort_2(unsorted)

    assert unsorted == expected

    unsorted = [2, 1, 3]
    expected = [1, 2, 3]

    bubble_sort_2(unsorted)

    assert unsorted == expected


def test_bubble_sort_2_reversed():
    unsorted = []
    expected = []

    bubble_sort_2(unsorted, True)

    assert unsorted == expected

    unsorted = [2, 1, 3]
    expected = [3, 2, 1]

    bubble_sort_2(unsorted, True)

    assert unsorted == expected
