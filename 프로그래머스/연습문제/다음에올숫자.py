def solution(common):
    answer = 0

    flag = True
    d = 1e9
    for i in range(len(common) - 1):
        if i == 0:
            d = common[i + 1] - common[i]
        else:
            if d != common[i + 1] - common[i]:
                flag = False
                break

    if flag:
        answer = common[-1] + d
    else:
        r = common[1] // common[0]
        answer = common[-1] * r


    return answer