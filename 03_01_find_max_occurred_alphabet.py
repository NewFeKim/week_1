#Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오

input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"
                      "q", "r", "s", "t", "u", "v", "w", "x", "y" "z"]


    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet

    # 이 부분을 채워보세요!
    return max_alphabet


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