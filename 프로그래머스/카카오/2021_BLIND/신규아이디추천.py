def solution(new_id):
    answer = ''

    # 1단계
    for i in range(len(new_id)):
        answer += new_id[i].lower()

    # 2단계
    tmp = ''
    for i in range(len(answer)):
        if answer[i].isalnum() or answer[i] in ['-', '_', '.']:
            tmp += answer[i]
    answer = tmp

    # 3단계
    tmp = ''
    for i in range(len(answer)):
        if i != 0 and answer[i] == '.' and tmp[-1] == '.':
            continue
        tmp += answer[i]
    answer = tmp

    # 4단계
    s = 0
    e = len(answer)
    if answer[0] == '.':
        s = 1
    if answer[-1] == '.':
        e = len(answer) - 1
    answer = answer[s:e]

    # 5단계
    if answer == '':
        answer += "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer