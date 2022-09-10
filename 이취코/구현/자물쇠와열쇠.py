# 2차원 리스트 90도 회전
def rotate(M, key):
    new_key = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[j][M - i - 1] = key[i][j]

    return new_key


# 모든 홈이 맞는지 확인
# 가운데 자물쇠만 확인
def check(wide_lock):
    length = len(wide_lock) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if wide_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)

    # 자물쇠의 3배 크기의 맵 생성 후 
    # 맵 중앙에 자물쇠를 박음
    # 모든 맵을 탐색 -> 자물쇠 기준 모든 영역 완전탐색
    wide_lock = [[0] * (N * 3) for _ in range(N * 3)]
    for i in range(N):
        for j in range(N):
            wide_lock[i + N][j + N] = lock[i][j]

    # 4번의 회전에 대해서 탐색
    for _ in range(4):
        # 회전
        key = rotate(M, key)
        for x in range(N * 2):
            for y in range(N * 2):
                # 자물쇠에서 (x, y)를 기준으로
                # (x, y) ~ (x + M, y + M)까지 key를 끼워넣음
                for i in range(M):
                    for j in range(M):
                        # 탐색영역에 열쇠를 끼어넣음
                        wide_lock[x + i][y + j] += key[i][j]

                # 자물쇠와 열쇠가 맞아떨어지면 종료
                if check(wide_lock):
                    return True

                # 끼웠던 열쇠 제거 -> 자물쇠 초기화
                for i in range(M):
                    for j in range(M):
                        wide_lock[x + i][y + j] -= key[i][j]

    return answer