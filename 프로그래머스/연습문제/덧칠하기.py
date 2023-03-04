def solution(n, m, section):
    answer = 0

    checked = [True] * (n + 1)
    for i in section:
        checked[i] = False

    i = 1
    while i <= n:
        if checked[i] is True:
            i += 1
        else:
            i += m
            answer += 1

    return answer