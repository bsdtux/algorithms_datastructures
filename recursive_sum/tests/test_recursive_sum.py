from recursive_sum import recursive_sum, recursive_sum_2


def test_recursive_sum():
    sum_list = []
    expected = 0

    result = recursive_sum(sum_list)

    assert result == expected

    sum_list = [1, 2, 3]
    expected = 6

    result = recursive_sum(sum_list)
    assert result == expected


def test_recursive_sum_2():
    sum_list = []
    expected = 0

    result = recursive_sum_2(sum_list)

    assert result == expected

    sum_list = [1, 2, 3]
    expected = 6

    result = recursive_sum_2(sum_list)
    assert result == expected
