input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        #index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    print(max_alphabet_index)
    return chr(max_alphabet_index+ord("a"))


result = find_max_occurred_alphabet(input)
print(result)







#my code
"""
input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    find_occurred_alphabet = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        char_index = ord(char) - ord("a")
        find_occurred_alphabet[char_index] += 1

    _num = 0
    for num in find_occurred_alphabet:
        if num < _num:
            _max = _num



    return "a"


result = find_max_occurred_alphabet(input)
print(result)

"""