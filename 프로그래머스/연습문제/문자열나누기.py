def solution(s):
    answer = 0
    x = ''
    other = ''

    for c in s:
        if x == '' or x[0] == c:
            x += c
        else:
            other += c
        if len(x) == len(other):
            answer += 1
            x = ''
            other = ''
    if x != '' or other != '':
        answer += 1

    return answer