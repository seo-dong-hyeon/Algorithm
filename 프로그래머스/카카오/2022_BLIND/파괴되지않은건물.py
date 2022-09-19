# 누적합 - imos법
# 각 쿼리가 특정 구간 [s, e] 내의 값을 갱신
# 일단 입장(s)과 퇴장(e)만 기록
# 나중에 한번에 쓸어내면서 원래 값을 복원
# ex), 0 ~ 2까지 N 감소
# [-N, 0, 0, N, 0, 0] 
# 1 ~ 3까지 M 감소
# [-N, -M, 0, N, M, 0] 
# 휩쓸기
# [-N, -M-N, -M-N, -M, 0, 0]
def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    # 누적합 배열
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
 
    for type, r1, c1, r2, c2, degree in skill:
        # type이 1이면 감소
        if type == 1:
            degree *= -1
        # 시작(r1, c1)과 끝(r2, c2)만 기록
        # [d 0 0 -d]
        # [0 0 0 0]
        # [0 0 0 0]
        # [-d 0 0 d]
        prefix_sum[r1][c1] += degree
        prefix_sum[r1][c2 + 1] += -degree
        prefix_sum[r2 + 1][c1] += -degree
        prefix_sum[r2 + 1][c2 + 1] += degree
 
    # 행 기준 누적합
    for i in range(len(prefix_sum) - 1):
        for j in range(len(prefix_sum[0]) - 1):
            prefix_sum[i][j + 1] += prefix_sum[i][j]
 
    # 열 기준 누적합
    for j in range(len(prefix_sum[0]) - 1):
        for i in range(len(prefix_sum) - 1):
            prefix_sum[i + 1][j] += prefix_sum[i][j]
 
    # 기존 배열과 합하여 전체 합산 확인
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] + prefix_sum[i][j] > 0:
                answer += 1
 
    return answer