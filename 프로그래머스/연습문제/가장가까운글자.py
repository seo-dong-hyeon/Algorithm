def solution(s):
    answer = []
    dic_pos = {}

    for i, c in enumerate(s):
        if c not in dic_pos:
            answer.append(-1)
            dic_pos[c] = i
        else:
            answer.append(i - dic_pos[c])
            dic_pos[c] = i

    return answer