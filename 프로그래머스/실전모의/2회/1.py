# 순열조합
from itertools import combinations

def solution(number):
    answer = 0

    for nCr in list(combinations(number, 3)):
        if nCr[0] + nCr[1] + nCr[2] == 0:
            answer += 1

    return answer