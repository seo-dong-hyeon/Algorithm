# imos 알고리즘
def solution(lines):
    answer = 0
    prefix_sum = [0] * 210

    # 체크 범위 조정
    # -100 <= x <= 100 -> 0 <= x <= 200
    for s, e in lines:
        prefix_sum[s + 100] += 1
        prefix_sum[e + 100] -= 1

    for i in range(len(prefix_sum) - 1):
        prefix_sum[i + 1] += prefix_sum[i] 

    for i in range(len(prefix_sum) - 1):
        if prefix_sum[i] >= 2:
            answer += 1

    return answer
