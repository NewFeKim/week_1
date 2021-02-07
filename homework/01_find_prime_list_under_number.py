"""
Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

"""

#보통 2, 3, 5, 7, 11, == 0

def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    number_array =[]
    for i in range(0, number + 1):
        if i == 2 or i == 3 or i ==5 or i == 7:
            number_array.append(i)
        elif i == 1 or i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            continue
        else:
            number_array.append(i)
    return number_array



input = 20
result = find_prime_list_under_number(input)
print(result)