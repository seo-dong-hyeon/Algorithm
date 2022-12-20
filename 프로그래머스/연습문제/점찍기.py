import math

def solution(k, d):
    answer = 0

    yPoint = d + 1
    for x in range(d + 1):
        xLength = math.pow(x * k, 2)
        if math.sqrt(xLength) > d:
            break
        for y in range(yPoint, -1, -1):
            if math.sqrt(xLength + math.pow(y * k, 2)) <= d:
                answer += y + 1
                yPoint = y
                break

    return answer