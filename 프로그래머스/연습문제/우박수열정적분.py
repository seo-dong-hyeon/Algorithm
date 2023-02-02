def solution(k, ranges):
    answer = []

    # 우박수열 구하기
    arr = []
    i = 0
    arr.append([i, k])
    while k != 1:
        i += 1
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        arr.append([i, k])

    # 각 구간의 넓이
    areas = []
    for i in range(len(arr) - 1):
        h = 1
        w = (arr[i][1] + arr[i + 1][1]) / 2
        areas.append(h * w)

    # 주어진 입력별 정적분 넓이
    for a, b in ranges:
        b = len(areas) + b
        # 넓이를 구할 수 없는 구간이면 -1.0
        area = sum(areas[a:b]) if b >= a else -1.0
        answer.append(area)

    return answer


print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))