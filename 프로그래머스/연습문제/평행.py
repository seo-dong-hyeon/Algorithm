def solution(dots):
    answer = 0
    
    for [a, b], [c, d] in [[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0, 3], [1, 2]]:
        incline1 = (dots[a][1] - dots[b][1]) / (dots[a][0] - dots[b][0]) if (dots[a][0] - dots[b][0]) != 0 else 1
        incline2 = (dots[c][1] - dots[d][1]) / (dots[c][0] - dots[d][0]) if (dots[c][0] - dots[d][0]) != 0 else 1
        if incline1 == incline2:
            return True
    
    return answer