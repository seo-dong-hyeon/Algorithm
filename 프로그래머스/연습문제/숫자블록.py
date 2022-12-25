import math

def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 0:
            answer.append(0)
        div = 1
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tmp = i // j
                if tmp > 10000000:
                    div = 1
                    continue
                else:
                    div = tmp
                    break
        answer.append(div)

    return answer