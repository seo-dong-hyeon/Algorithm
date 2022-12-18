def solution(k, tangerine):
    answer = 0
    dic_num_cnt = {}

    for num in tangerine:
        if num not in dic_num_cnt:
            dic_num_cnt[num] = 0
        dic_num_cnt[num] += 1

    for num, cnt in sorted(dic_num_cnt.items(), key=lambda x : x[1], reverse=True):
        answer += 1
        k -= cnt
        if k <= 0:
            break

    return answer