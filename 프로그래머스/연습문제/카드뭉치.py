def solution(cards1, cards2, goal):
    answer = ''

    idx1 = 0
    idx2 = 0
    for i in goal:
        if idx1 < len(cards1) and cards1[idx1] == i:
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == i:
            idx2 += 1
        else:
            answer = "No"
            break

    if answer == '':
        answer = "Yes"

    return answer