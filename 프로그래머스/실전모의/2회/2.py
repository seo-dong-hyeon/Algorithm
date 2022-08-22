# 두수의 합
def solution(topping):
    answer = 0
    left = {}
    right = {}
    leftCnt = 0
    rightCnt = 0

    for t in topping:
        if t not in right:
            right[t] = 0
            rightCnt += 1
        right[t] += 1

    for t in topping:
        if t not in left:
            left[t] = 0
            leftCnt += 1
        left[t] += 1
        right[t] -= 1
        if right[t] == 0:
            rightCnt -= 1
        if leftCnt == rightCnt:
            answer += 1
        
    return answer