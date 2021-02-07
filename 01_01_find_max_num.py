input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num



    """
    _max = 0
    for i in array:
        _num = i
        if _max < _num:
            _max = _num
    """

    return num


result = find_max_num(input)
print(result)