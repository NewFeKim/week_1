
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1


    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))




# my code
"""
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!

    #str.isalpha(string[0])
    for k in string:
        if k.isalpha() == True:
            alphabet_occurrence_array[ord(k)-ord("a")] += 1


    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
"""
#string = "hello my name is sparta"



"""
tip
 문자인지 확인하는 법
 str.isalpha()
 "a".isalpha()
 


"""