def check_valid(pillow, beam):
    n = len(pillow)

    for i in range(n):
        for j in range(n):
            if pillow[i][j] == True:
                # 바닥 위에 있거나, 다른 기둥 위에 있거나, 보의 한쪽 끝 부분 위에 있지 않으면 조건 만족x
                if not (i == n - 1 or (i + 1 < n and pillow[i + 1][j] == True) or (j - 1 >= 0 and beam[i][j - 1] == True) or beam[i][j] == True):
                    return False
            if beam[i][j] == True:
                # 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있지 않으면 조건 만족x
                if not ((i + 1 < n and pillow[i + 1][j] == True) or (i + 1 < n and j + 1 < n and pillow[i + 1][j + 1] == True) or (j - 1 >= 0 and j + 1 < n and beam[i][j - 1] == True and beam[i][j + 1] == True)):
                    return False
    return True


def solution(n, build_frame):
    answer = []
    pillow = [[False] * (n + 1) for _ in range((n + 1))]
    beam = [[False] * (n + 1) for _ in range((n + 1))]

    for x, y, a, b, in build_frame:
        # 주어진 좌표값 -> 리스트 상에서 인덱스
        y = n - y
        x, y = y, x
        if a == 0:
            pillow[x][y] = True if b == 1 else False
            # 조건을 만족하지 못하면 원래대로 되돌림
            if not check_valid(pillow, beam):
                pillow[x][y] = not pillow[x][y]
        else:
            beam[x][y] = True if b == 1 else False
            # 조건을 만족하지 못하면 원래대로 되돌림
            if not check_valid(pillow, beam):
                beam[x][y] = not beam[x][y]

    length = len(pillow)
    for i in range(length):
        for j in range(length):
            # 서로 독립적으로 존재할 수 있으므로
            # elif X -> if문 2개
            if pillow[i][j]:
                answer.append([j, n - i, 0])    # 주어진 좌표값 -> 리스트 상에서 인덱스
            if beam[i][j]:
                answer.append([j, n - i, 1])    # 주어진 좌표값 -> 리스트 상에서 인덱스

    answer.sort(key=lambda x : (x[0], x[1], x[2]))

    return answer