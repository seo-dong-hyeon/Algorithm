def solution(a, b, n):
    answer = 0

    while n >= a:
        cnt = n // a
        answer += cnt * b
        n = n  - (cnt * a) + (cnt * b)

    return answer