max_diff = -1       # 최대 점수차
max_comb = [0] * 11 # 최대 점수차 일때 맞춘 화살 조합
comb = [0] * 11     # 현재 화살 조합

# dfs(n, info, 점수판 index, 남은 화살 개수, 라이언 점수, 어퍼치 점수)
def dfs(n, info, idx, rest, score_lion, score_apach):
    global max_diff, max_comb, comb
    if idx == 10 or rest == 0:  # 점수판 끝까지 갔거나 남은 화살이 없다면
        if score_lion > score_apach:    # 라이언 점수가 더 높다면
            if score_lion - score_apach > max_diff or max_diff == -1:   # 최대 점수차거나 최대 점수가 갱신이 안된 경우라면
                max_diff = score_lion - score_apach # 최대 점수차 갱신
                max_comb = comb.copy()  # 최대 점수차 일때 화살 조합 갱신
                if rest > 0:    # 남은 화살이 있다면
                    max_comb[10] += rest    # 마지막 과녁에 맞춘 걸로 가정
            elif score_lion - score_apach == max_diff:  # 최대 점수차와 같다면
                if rest > 0:    # 남은 화살이 있다면
                    max_comb[10] += rest    # 마지막 과녁에 맞춘 걸로 가정
                for i in range(n):  # 가장 낮은 점수를 더 많이 맞춘 조합으로 갱신
                    if comb[11 - i - 1] > max_comb[11 - i - 1]:
                        max_comb = comb.copy()
                        break
                    elif max_comb[11 - i - 1] > comb[11 - i - 1]:
                        break
        return

    score = 10 - idx    # 획득 점수
    if rest >= info[idx] + 1:   # 남은 화살로 현재 점수를 얻을 수 있다면
        comb[idx] = info[idx] + 1   # 현재 과녁을 어퍼치보다 1개 화살을 더 사용하여 맞춤
        if info[idx] > 0:   # 현재 과녁에 어퍼치의 화살이 있다면
            dfs(n, info, idx + 1, rest - (info[idx] + 1), score_lion + score, score_apach - score)  # 어퍼치 점수 감소하며 진행
        else:               # 현재 과녁에 어퍼치의 화살이 없다면
            dfs(n, info, idx + 1, rest - (info[idx] + 1), score_lion + score, score_apach)  # 그대로 진행
        comb[idx] = 0   # 화살 조합 초기화
    dfs(n, info, idx + 1, rest, score_lion, score_apach)    # 라이언이 현재 과녁을 맞추지 못했다고 가정하여 진행


def solution(n, info):
    answer = []
    global max_diff, max_comb, comb

    # 어퍼치 총점수 계산
    score_apach = 0
    for i in range(11):
        score_apach += (10 - i) if info[i] > 0 else 0

    dfs(n, info, 0, n, 0, score_apach)

    if max_diff == -1:  # 라이언이 어퍼치보다 큰 점수를 못 얻은 경우
        answer.append(-1)
    else:
        answer = max_comb

    return answer