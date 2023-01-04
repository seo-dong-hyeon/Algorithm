import math

# 여러 수의 최대공약수
def getGCD(array):
    _gcd = array[0]

    for i in array:
        _gcd = math.gcd(_gcd, i)

    return _gcd


def checkDivision(array, divisor):
    for i in array:
        if i % divisor == 0:
            return -1
    return divisor


def solution(arrayA, arrayB):
    answer = 0

    a_gcd = getGCD(arrayA)
    b_gcd = getGCD(arrayB)

    answer = max(answer, checkDivision(arrayA, b_gcd))
    answer = max(answer, checkDivision(arrayB, a_gcd))

    return answer