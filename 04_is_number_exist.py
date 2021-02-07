#my code
"""
input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!

    for num in array:
        if num == number:
            return True
        else:
            continue

    return False


result = is_number_exist(3, input)
print(result)
"""

input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for element in array: #array의 길이만큼 아래 연산이 실행된다
        if number == element: # 비교 연산 1번 실행
            return True     # N * 1 = N 만큼
    return False


result = is_number_exist(3, input)
print(result)