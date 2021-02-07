"""
문제설명
Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '✕' 혹은

'+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.

단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.
"""

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum

    # 이 부분을 채워보세요!



result = find_max_plus_or_multiply(input)
print(result)




#my code
"""
input = [0, 3, 5, 6, 1, 2, 4]

#0과 1이 나오면 더하기 그리고 그외엔 곱하기

def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!

    sum = 0

    for _num in array:

        if _num == 0:
            sum += _num
        elif _num == 1:
            sum += _num
        else:
            if sum == 0:
                sum += _num
            else:
                sum *= _num
        print(sum)



    return sum


result = find_max_plus_or_multiply(input)
print(result)
"""