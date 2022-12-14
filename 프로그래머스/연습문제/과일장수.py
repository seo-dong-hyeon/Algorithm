def solution(k, m, score):
    answer = 0

    score = sorted(score, reverse=True)
    cnt = 0
    min_score = 1e9
    for i in score:
        min_score = min(min_score, i)
        cnt += 1
        if cnt == m:
            answer += min_score * m
            cnt = 0

    return answer