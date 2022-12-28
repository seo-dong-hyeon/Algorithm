# 미완성
from typing import List

def get_total(a, b, t):
    return (t // a) * b + b


def solution(fees: List[List[int]], t: int) -> List[int]:
    answer = []
    
    ab = []
    for x, y in fees:
        flag = False
        for a in range(1, 1000000 + 1):
            left = 1
            right = 1000000000
            flag = False
            while left <= right:
                mid = (left + right) // 2
                total = get_total(a, mid, y)
                if total > x:
                    right = mid - 1
                elif total < x:
                    left = mid + 1
                else:
                    flag = True
                    break
            if flag:
                ab.append([a, mid])

    if len(ab) == 0:
        answer.append(-1)
    else:
        for a, b in ab:
            answer.append(get_total(a, b, t))
        answer.sort()
        answer = [answer[0], answer[-1]]

    return answer

print(solution([[3, 40000],[5,60000]], 2))

# a = 10, b = 1000
# 0 ~ 9 : 1000
# 10 ~ 19 : 1000 + 1000 = 2000
# 20 ~ 29 : 2000 + 1000 = 3000

# a = 9, b = 1000
# 0 ~ 8 : 1000
# 9 ~ 17 : 1000 + 1000 = 2000
# 18 ~ 26 : 2000 + 1000 = 3000
# 27 ~  : 3000 + 1000 = 4000

