import math

# 즉각적인 소수 판별
def is_prime_number(n):
    if n < 2:
        return False
        
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# 10진수 -> k진수
def convert(n, k):
    rev_base = ""

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n, k):
    answer = 0
    # k진수로 변환
    nums = convert(n, k)

    P = ""
    for num in nums:
        # 0이면 P가 소수인지 검사
        if num == "0":
            if len(P) != 0:
                P = int(P)
                if is_prime_number(P):
                    answer += 1
                P = ""
        # 0이 아니면 숫자를 붙임
        else:
            P += num

    # 마지막 숫자가 0이 아닌 경우
    # 그동안 쌓인 숫자 검사
    if len(P) != 0:
        P = int(P)
        if is_prime_number(P):
            answer += 1

    return answer