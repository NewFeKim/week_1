"""
Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
만약 그런 문자가 없다면 _ 를 반환하시오.

"""

input = "abacabade"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!

    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    print(not_repeating_character_array)

    for char in string:
        if char in not_repeating_character_array:
            return char





    return "_"


result = find_not_repeating_character(input)
print(result)


"""

    for char in string:
        _check = char
        if string[0]:
            break
        elif 

        for k in string:
            if char == k:
                break
            else:
                return char
"""